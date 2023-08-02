
# Violation Codes

{'title': 'Violation Codes', 'content': 'Servers with the truth.enforce option enabled will use the Rust truth detector to periodically check the movements of players and kick them when they detect strange behaviour.\nEvery few server frames a ray is cast 0.5 meters (units?) above your head, between your previous and your next position. When the distance divided by the delta time of your movement exceeds 20, this Δdistance/Δtime value is added to your violation number. If the ray cast collides with a solid it will add 100 to the violation number.\nNot only the violation number, but also the amount of which the number increases in a short time, will get you kicked.\n \nThanks to mistad for this in-depth explanation and code.'}
