import json
import re
import time
from typing import Optional, List
from dataclasses import dataclass, field
import numpy as np
import requests
import pandas as pd
from tqdm.autonotebook import tqdm

# change these variables to change the fandom instance & character category/ies
FANDOM_SITE = 'rust'
CATEGORY = 'Weapons'
CATEGORIES_RULES = ['gameplay','guides','Environment','Mechanics','Maps']
JSON_FILE = f"projects/{FANDOM_SITE}.json"
FANDOM_URL = f'https://{FANDOM_SITE}.fandom.com'
API_URL = FANDOM_URL + '/api.php'

NAMESPACES = [
    ('0', 'Article'),
    ]


def remove_suffix(cell, suffix):
    if cell and cell.endswith(suffix):
        l = len(suffix)
        cell = cell[:-l]
    else:
        pass
    return cell


def remove_suffixes(df, col_list, suffix_list):
    for col in col_list:
        for suffix in suffix_list:
            df[col].loc[df[col].str.endswith(suffix, na=False)] = (df[col].loc[df[col].str.endswith(suffix, na=False)]
                                                         .apply(lambda x: remove_suffix(x, suffix))
                                                         .str.strip())
    return df

# These functions are for getting all pages in a category and their infoboxes.

def make_list_chunks(lst, n=50):
    """split a list up into sublist chunks of size n (default 50)"""
    return [lst[i:i + n] for i in range(0, len(lst), n)]

@dataclass
class WikiAPI:
    '''A base class for querying a fandom Wiki'''
    fandom_site: str = FANDOM_SITE
    fandom_url: str = FANDOM_URL
    api_url: str = API_URL
    category: Optional[str] = CATEGORY
    categories: Optional[list] = field(default_factory=list)
    namespaces: List = field(default_factory=list)
    params: dict = field(default_factory=dict)

    def __post_init__(self):
        self.namespaces = NAMESPACES
        self.params = {'action': 'query',
                       'format': 'json',
                      }

    def scrape(self):
        pass

    def parse(self):
        pass

    def build(self):
        self.scrape()
        self.parse()

    def get_all_namespaces(self, api_url=API_URL):
        params = {'action': 'query',
                  'format': 'json',
                  'meta': 'siteinfo',
                  'siprop': 'namespaces',
                  }
        r = requests.get(api_url, params=params)
        data = json.loads(r.text)
        namespaces = data['query']['namespaces']
        nses = [(k, v.get('canonical', '*')) for k, v in namespaces.items()]
        return nses

    def get_all_pages(self, namespace=None):
        '''Get all pages from a particular namespace (defaults to articles).'''
        params = {'action': 'query',
                'format': 'json',
                'list': 'allpages',
                'aplimit': '500',
                'apfilterredir': 'nonredirects',
                'apcontinue': '0',
                }
        if namespace is None:
            namespace = 0
        params.update({'apnamespace': namespace})
        all_pages = []
        cont = "0"
        while cont != "1":
            r = requests.get(API_URL, params=params)
            data = json.loads(r.text)
            pages = data['query']['allpages']
            pages = [(x['pageid'], x['title']) for x in pages]
            all_pages.extend(pages)
            try:
                apcontinue = data['continue']['apcontinue']
            except KeyError:
                apcontinue = "1"
            cont = apcontinue
            params.update({'apcontinue': apcontinue})
            time.sleep(1)
        return all_pages


@dataclass
class WikiCategory(WikiAPI):
    '''Given a category or list of categories, get the subcategories and the pages in those subcategories.
    Queries the API for both categories & pages at the same time.'''
    recursive: bool = True
    group_pages: bool = False

    def __post_init__(self):
        super().__post_init__()
        self.params.update({'list': 'categorymembers',
                            'cmtype': 'subcat|page',
                            'cmtitle': f'Category:{self.category}',
                            'cmlimit': 500,
                            'cmcontinue': '',
                            })
        if not self.categories:
            self.categories = [self.category]

    def scrape(self):
        self.category_members = self.get_category_members()
        self.subcats = self.category_members.get('subcats', None)
        self.pages = self.category_members.get('pages', None)
        if not self.group_pages:
            self.pageids = [x[0] for x in self.pages]
            self.titles = sorted([x[1] for x in self.pages])

    def get_category_members(self, categories=None, recursive=None, group_pages=None, params=None):
        # 处理参数的默认值
        if categories is None:
            categories = self.categories
        if recursive is None:
            recursive = self.recursive
        if group_pages is None:
            group_pages = self.group_pages
        if params is None:
            params = self.params
        items = {}
        items['categories'] = categories
        items['subcats'] = []
        if group_pages:
            items['pages'] = {}
        else:
            items['pages'] = []

        print('Retrieving category members:\n')
        # 对每个类别进行遍历
        for category in tqdm(items['categories']):
            # 设置API请求的参数
            params['cmtitle'] = f'Category:{category}'
            params['cmcontinue'] = 0
            # 循环直到所有成员都被获取完
            while params['cmcontinue'] != 1:
                r = requests.get(API_URL, params=params)
                # print(r.url)
                data = json.loads(r.text)
                results = data['query']['categorymembers']
                # 获取子类别的标题
                subcats = [x['title'].replace('Category:', '') for x in results if int(x['ns']) == 14]
                items['subcats'].extend(subcats)
                # 获取页面的标题和页面ID
                pages = [(x['pageid'], x['title']) for x in results if int(x['ns']) == 0]
                # 根据是否分组页面进行不同的处理
                if group_pages:
                    if not items['pages'].get(category, None):
                        items['pages'][category] = []
                    items['pages'][category].extend(pages)
                else:
                    items['pages'].extend(pages)
                # 如果选择了递归，将子类别添加到类别列表中
                if recursive:
                    # append new categories to the category list
                    items['categories'].extend(subcats)
                # 检查是否有更多结果，获取下一页的cmcontinue值
                if 'batchcomplete' in data.keys():
                    params['cmcontinue'] = 1
                else:
                    params['cmcontinue'] = data['continue']['cmcontinue']
            # 暂停1秒以避免连续请求造成过多负载
            time.sleep(1)
        # 去重并排序页面和子类别
        if not group_pages:
            for k, v in items.items():
                items[k] = sorted(list(set(v)))
        return items


@dataclass
class WikiInfobox(WikiAPI):
    '''Given a list of wikipages, scrape their infoboxes.'''
    pages: Optional[list] = field(default_factory=list)
    titles: Optional[list] = field(default_factory=list)
    recursive: bool = True
    by_category: bool = True
    standardize_case: bool = True
    alert_empty: bool = True

    def __post_init__(self):
        super().__post_init__()
        self.params.update({
            'prop': 'revisions',
            'rvprop': 'content',
            'rvsection': '0',
            'rvslots': '*',
        })
        if self.pages and not self.titles:
            self.titles = [x[1] for x in self.pages]

    def scrape(self):
        if self.by_category:
            if not self.categories:
                self.categories = [self.category]
            if not self.pages and not self.titles:
                wikicat = WikiCategory(categories=self.categories, recursive=self.recursive)
                wikicat.scrape()
                self.pages = wikicat.pages
                self.pageids = wikicat.pageids
                self.titles = wikicat.titles
            elif not self.titles:
                self.pageids = [x[0] for x in self.pages]
                self.titles = [x[1] for x in self.pages]
        if self.titles:
            self.params.update({'titles': self.titles})
            self.raw_infoboxes = self.get_raw_infoboxes()
            self.matched_raw_infoboxes = self.match_names_to_infoboxes()

    def parse(self):
        if self.titles:
            self.unsorted_infoboxes = self.get_parsed_infoboxes()
            self.infoboxes = self.sort_infoboxes_by_template()
            self.dfs = self.build_dfs_infobox()
            if len(self.dfs) == 1:
                self.df = list(self.dfs.values())[0]

    def get_raw_infoboxes(self, titles=None, params=None):
        '''From a list of titles, get the raw json for their infoboxes'''
        if titles is None:
            titles = self.titles
        try:
            assert type(titles) == list
        except AssertionError:
            raise TypeError
        if params is None:
            params = self.params

        # break up titles into chunks of 50 or fewer
        title_chunks = make_list_chunks(titles)

        raw_infoboxes = {}
        print('Retrieving infoboxes for each page title:')
        for chunk in tqdm(title_chunks):
            time.sleep(1)  # add sleep so don't overwhelm server
            title_list = '|'.join([x for x in chunk])
            params.update({'titles': title_list})
            r = requests.get(API_URL, params=params)
            json_values = r.json()
            pages = json_values['query']['pages']
            boxes = {int(k): v['revisions'][0]['slots']['main']['*'] for k, v in pages.items() if int(k) > 0}
            # warn if missing infoboxes
            missing_boxes = {k: v for k, v in pages.items() if int(k) < 1}
            if missing_boxes:
                for v in missing_boxes.values():
                    print(f"Infobox page missing: {v['title']}")
            raw_infoboxes.update(boxes)

        return raw_infoboxes

    def process_value(self, val):
        """within the context of an infobox to be parsed, clean up the value after the '=' sign."""
        val = val.replace("[[","")
        val = val.replace("]]","")
        val = val.replace("}}","")
        val = val.replace("{{","")
        val = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", val)
        val = val.replace("()","")

        val = val.lstrip('*').strip()

        #remove any training white spaces left
        ##if we have a br the k becomes an array

        if any(x in val for x in ['<br />', '<br>', '<br/>']):
            val = val.replace('<br />', '<br>').replace('<br/>', '<br>')
            val = val.split('<br>')
            val = [x.strip() for x in val]

        # transform true/false to boolean
        if type(val) == str and val.lower() == 'true':
            val = True
        elif type(val) == str and val.lower() == 'false':
            val = False
        return val

    def parse_infobox(self, info_json, standardize_case=None):
        if standardize_case is None:
            standardize_case = self.standardize_case
        infoboxes = {}
        infobox_name = ''
        k = ''
        json_lines = info_json.splitlines()
        for i, line in enumerate(json_lines):
            is_list = False
            if re.findall(r'\{\{Infobox.*?', line):
                infobox_name = re.findall(r'Infobox.*', line)[0].strip().replace('_', ' ')
                infoboxes[infobox_name] = {}
            elif line.startswith('|'):
                # process k
                k = line.partition('=')[0].strip()[1:]
                k = k.strip()
                if self.standardize_case:
                    k = k.lower()

                # process val
                val1 = line.partition('=')[-1].strip()
                val = self.process_value(val1)
                if type(val) == str and (val1.startswith('*') or not len(val)):
                    is_list = True
                    if val1.startswith('*'):
                        assert len(val1.split('*')) == 2
                        item_1 = val.lstrip('*').strip()
                        val = [item_1]
                    elif json_lines[i+1].startswith('*'):
                        val = []
                    else:
                        is_list = False
                    if is_list:
                        assert json_lines[i+1].startswith('*')
                        counter = 0
                        idx = i
                        while counter < 20:
                            # look ahead for other list members, stopping at next parameter field
                            if json_lines[idx+1].startswith('*'):
                                new_item = self.process_value(json_lines[idx+1])
                                val.append(new_item)
                                idx += 1
                                counter += 1
                            else:
                                break

                elif type(val) == str:
                    assert '*' not in val

                #process k
                if not infobox_name:
                    print('no infobox name:', k, val[:20])
                else:
                    infoboxes[infobox_name][k] = val

        return infoboxes

    def match_names_to_infoboxes(self,
                                 categories=None,
                                 pages=None,
                                 titles=None,
                                 pageids=None,
                                 infoboxes=None):
        '''Uses pageids to match title/name tuple to raw infobox json.'''
        if categories is None:
            categories = self.categories
        if pages is None:
            pages = self.pages
        if titles is None:
            if not hasattr(self, 'titles') or not self.titles:
                titles = [x[1] for x in pages]
            else:
                titles = self.titles
        if pageids is None:
            if not hasattr(self, 'pageids') or not self.pageids:
                pageids = [x[0] for x in pages]
            else:
                pageids = self.pageids
        if infoboxes is None:
            infoboxes = self.raw_infoboxes
        matched_raw_infoboxes = {}
        for pid in pageids:
            title = next(x[1] for x in pages if x[0] == pid)
            matched_raw_infoboxes[(pid, title)] = infoboxes[pid]
        return matched_raw_infoboxes

    def get_parsed_infoboxes(self, titles=None, raw_infoboxes=None, standardize_case=None):
        '''Parses the raw infoboxes into dicts from matched title json dict.'''
        if titles is None and raw_infoboxes is None:
            titles = self.titles
        if raw_infoboxes is None:
            raw_infoboxes = self.raw_infoboxes
        if standardize_case is None:
            standardize_case = self.standardize_case

        matched_infoboxes = self.match_names_to_infoboxes(titles=titles, infoboxes=raw_infoboxes)

        infoboxes = {k: self.parse_infobox(v, standardize_case=standardize_case) for k, v in matched_infoboxes.items()}
        return infoboxes

    def get_infoboxes_for_title(self, title, standardize_case=None, parsed=True):
        """For a single title, get the article infoboxes. Do not use to iterate!
        Use chunking via `self.get_parsed_infoboxes()` instead."""
        if standardize_case is None:
            standardize_case = self.standardize_case
        title = '_'.join(title.split())
        fullurl = '/'.join([FANDOM_URL, title])
        r = requests.get(fullurl, params={'action': 'raw',
                                          'section': '0',
                                          'format': 'json',
                                          })
        page = r.text
        if parsed:
            parsed_infobox = self.parse_infobox(page, standardize_case=standardize_case)
            return parsed_infobox
        else:
            return page

    def write_infobox_json(self, categories=None, df=None):
        '''Output infobox dict to json file'''
        if categories is None:
            categories = self.categories
        if df is None:
            df = next(iter(self.dfs.values()))
        df = df.set_index('page_title', drop=True)
        json_data = df.to_json(indent=4, orient='index')
        with open(JSON_FILE, 'w') as f:
            f.write(json_data)

    def sort_infoboxes_by_template(self, infoboxes=None, alert_empty=None):
        if alert_empty is None:
            alert_empty = self.alert_empty
        if infoboxes is None:
            infoboxes = self.unsorted_infoboxes
        sorted_infoboxes = {}
        for k, v in infoboxes.items():
            for infobox_name, infobox in v.items():
                if not sorted_infoboxes.get(infobox_name, None):
                    sorted_infoboxes[infobox_name] = {}
                sorted_infoboxes[infobox_name][k] = infobox
        if alert_empty:
            empty = [k for k, v in infoboxes.items() if not v.values()]
            if len(empty):
                print(f"These entries are missing infoboxes and will not be in df: {empty}")
        return sorted_infoboxes

    def build_df_infobox(self, infoboxes):
        df = pd.DataFrame.from_dict(infoboxes, orient='index')
        df.index.set_names(["pageid", "page_title"], inplace=True)
        df = df.reset_index()
        df.pageid = df.pageid.astype(int)
        df = df.replace('PAGENAME', np.NaN)
        return df

    def build_dfs_infobox(self, infoboxes=None):
        if infoboxes is None:
            infoboxes = self.infoboxes
        dfs_dict = {}
        for infobox_name, val in infoboxes.items():
            dfs_dict[infobox_name] = self.build_df_infobox(val)
            df_name = 'df_' + infobox_name.replace('Infobox ', '').lower()
            setattr(self, df_name, dfs_dict[infobox_name])
        return dfs_dict


import re

def sanitize_filename(filename):
    """
    清理文件名，将空格替换为下划线，将斜杠替换为下划线，并修改其他常见的非法字符。

    Args:
    filename: 要清理的文件名。

    Returns:
    清理后的文件名。
    """

    # 将空格替换为下划线。
    filename = re.sub(r' ', '_', filename)

    # 将斜杠替换为下划线。
    filename = re.sub(r'/', '_', filename)
    filename = re.sub(r'\\', '_', filename)

    # 修改其他常见的非法字符。
    filename = re.sub(r'[!@#$%^&*(){}:;<>,.?]', '', filename)

    # 返回清理后的文件名。
    return filename

def process_section(sections, depth=1):
    markdown_sections = ""

    for section in sections:
        title = section.get('title', '')
        content = section.get('content', '')

        markdown_sections += f"{'#' * depth} {title}\n\n{content}\n"

        subsections = section.get('sections', [])
        if subsections:
            markdown_sections += process_section(subsections, depth + 1)
        
    return markdown_sections

import copy
from bs4 import BeautifulSoup, NavigableString, Tag
from fandom import FandomPage
import re

class FandomPageParser(FandomPage):
  @property
  def content(self):
    """
    Text content of each section of the page, excluding images, tables,
    and other data. The content is returned as dict, imitating the section and
    subsection structure of the page.

    .. note::
      If you just want the plain text of the page without the section structure, you can use FandomPage.plain_text

    :returns: :class:`dict`
    """
    def clean(content):
      # 清洗内容的辅助函数，去除不需要的字符和标记
      keys = list(content.keys())
      if 'sections' in content: keys.remove('sections')

      for key in keys:
        if content[key] != "":
          # 替换特殊字符
          content[key] = re.sub(u'\xa0', ' ', content[key])
          # 移除方括号标记
          content[key] = re.sub(r'\[.*?\]', '', content[key])
          # 简化多余空格和换行符
          content[key] = re.sub(' +', ' ', content[key])
          content[key] = re.sub('\n+', '\n', content[key])
          # 如果内容只包含换行符，则设为空字符串
          if content[key] == "\n":
            content[key] = ""
          else:
            # 移除首尾的换行符
            content[key] = content[key][1:] if content[key][0] == '\n' else content[key]
            content[key] = content[key][:-1] if content[key][-1] == '\n' else content[key]

      if 'sections' in content:
        # 递归清洗每个子节
        for s in content['sections']:
          s = clean(s)

      return content

    if not getattr(self, '_content', False):
      html = self.html
      soup = BeautifulSoup(html, 'html.parser')

       # 移除页面中的一些不需要的元素，如infobox，toc，message_boxes等
      page_content = copy.copy(soup.find('div', class_="mw-parser-output"))

      infoboxes = page_content.find_all('aside', class_="portable-infobox")
      infobox_content = ""
      for box in infoboxes:
          infobox_content += box.text
          box.decompose()

      toc = page_content.find('div', id='toc')
      if toc: toc.decompose()

      message_boxes = page_content.find_all('table', class_="messagebox")
      for box in message_boxes:
        box.decompose()

      captions = page_content.find_all('p', class_="caption")
      for caption in captions:
        caption.decompose()

      nav_boxes = page_content.find_all('table', class_="navbox")
      for box in nav_boxes:
        box.decompose()

      content = {'title': self.title}
      level_tree = [content]
      current_level = 1

      # 初始化next_node为页面内容的第一个节点
      next_node = page_content.contents[0]
      while isinstance(next_node, NavigableString) or next_node.name in ["div", "figure"]:
        # 跳过一些节点，如文本节点、div节点等
        next_node = next_node.nextSibling

      # 初始化节的文本内容为空字符串
      section_text = ""
      while True:
        if next_node is None:
          # 如果到达页面内容的末尾，则将当前节的文本内容设置为section_text，并结束循环
          level_tree[-1]['content'] = section_text
          break
        elif isinstance(next_node, Tag):
          if re.match(r'^h\d+', next_node.name):
          #if next_node.name[0] == 'h':
            # 如果当前节点是一个标题节点
            level_tree[-1]['content'] = section_text
            header = next_node.text
            header_level = int(next_node.name[1])
            if header_level > current_level:
              # 如果当前标题级别高于当前级别，则添加一个新的子节
              level_dif = abs(header_level - current_level)
              for _ in range(level_dif):
                level_tree[-1]['sections'] = [{'title':header}]
                level_tree.append(level_tree[-1]['sections'][0])
            elif header_level == current_level:
              # 如果当前标题级别与当前级别相同，则在同一层级下添加一个新的子节
              level_tree[-2]['sections'].append({'title':header})
              level_tree[-1] = level_tree[-2]['sections'][-1]
            else:
              # 如果当前标题级别低于当前级别，则返回到正确的层级，并添加一个新的子节
              level_dif = header_level - current_level
              level_tree = level_tree[:level_dif]
              if len(level_tree) >= 2:
                level_tree[-2]['sections'].append({'title':header})
                level_tree[-1] = level_tree[-2]['sections'][-1]

            section_text = ""
            # 清空section_text
            current_level = header_level
          #elif next_node.name == 'div':
          # 如果当前节点不是printfooter类的节点，则将其文本内容添加到section_text中
          elif (not next_node.has_attr('class')) or (next_node['class'][0] != "printfooter"):
            # 如果是数据库表格，处理成文本
            if next_node.name == 'table' and next_node.has_attr('class') and next_node['class'][0] == "article-table":
                data_list = []

                #找到表头
                headers = next_node.select('th')
                header_names = [header.text.strip() for header in headers]

                # 找到数据行
                rows = next_node.select('tr')
                for row in rows:
                    cells = row.select('td')
                    if len(cells) == len(headers):
                        data = {}
                        for i, cell in enumerate(cells):
                            data[header_names[i]] = cell.text.strip()
                        data_list.append(data)

                final_text = ""
                # 输出每个表格中的数据
                for data in data_list:
                    for key, value in data.items():
                        result = f"{key}: {value}"
                        final_text += result
                    final_text += "\n"
                
                section_text += final_text 
            else:
                section_text += "\n"+next_node.get_text()
        next_node = next_node.nextSibling

      # 如果当前节点不是printfooter类的节点，则将其文本内容添加到section_text中
      if infobox_content != "": content['infobox'] = infobox_content

      self._content = clean(content)
    return self._content


if __name__ == "__main__":

    #page = FandomPageParser(FANDOM_SITE, 'en', title='Ammunition', redirect=True, preload=False)
    #print(page.html)
    #ections = page.content['sections']

    #print(f'Getting {CATEGORIES_RULES} infoboxes from fandom site {FANDOM_SITE}\n')
    # create WikiInfobox instance with default values

    #wi = WikiCategory(categories=CATEGORIES_RULES, recursive=False)
    #wi = WikiInfobox(categories=CATEGORIES, recursive=False)
    #wi.build()

    #wi.scrape()
    #pages = wi.pages

    import fandom
    import json

    wiki = WikiAPI()

    page_infos = wiki.get_all_pages()

    fandom.set_wiki(FANDOM_SITE)

    for pageid,pagename in page_infos:
        time.sleep(1)
        #page = fandom.page(pagename)
        page = FandomPageParser(FANDOM_SITE, 'en', title=pagename, redirect=True, preload=False)
        
        #额外获取分类信息
        query_params = {
            'action': 'query',
            'wiki': FANDOM_SITE,
            'lang': page.language,
            'redirects': True,
            'titles': page.title,
            'prop': 'categories'
        }

        from fandom.util import _wiki_request

        request = _wiki_request(query_params)
        if 'categories' in request['query']['pages'][str(page.pageid)]:
            # 包含'categories'键
            categories = request['query']['pages'][str(page.pageid)]['categories']
        else:
            # 不包含'categories'键
            categories = []  # 或其他处理方式

        categroy_text = []
        for categroy in categories:
            title = categroy['title'].replace('Category:', '')
            categroy_text.append(f"{title}")

        categroy_result = ",".join(categroy_text)        
        categroy_result = sanitize_filename(categroy_result)

        import json

        newfilename = sanitize_filename(pagename)

        print("try logging in file:" + newfilename)
        with open(f"data/{newfilename}({categroy_result}).md", "w", encoding='utf-8') as f:
            try:
                # 合并 `categories` 中的数据到 `page.content`

                markdown = ''
                if ('sections' in page.content):
                    sections = page.content['sections']
                    markdown = process_section(sections=sections)
                else:
                    markdown = f"\n{'#'} {page.title}\n\n{page.content}\n"
                

                #page.sections = categories + page.sections
                #page.content['categories'] = categories

                #from tabulate import tabulate
                #table = []
                #for key, value in page.content.items():
                #    table.append([key, value])

                #markdown_table = tabulate(table, tablefmt="pipe", headers=["Key", "Value"])

                f.write(markdown)
            except Exception as e:
                print(f"file {newfilename} data is not json, error: {e}")

