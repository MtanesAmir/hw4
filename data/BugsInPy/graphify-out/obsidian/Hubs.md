# Hubs (Subject 10)

According to subject 10 of the Lecture Summary, **Hubs** represent bottleneck nodes in the codebase architecture. All information flows through these nodes. Although they may have few direct outgoing transitions, they are critical passage points and represent significant architectural dependencies.

## Top Hubs in BugsInPy

| Rank | Hub Node | Betweenness Score | Origin File | Location |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [[BugsInPy README]] | 0.172 | [README.md](README.md) | None |
| 2 | [[verify.sh]] | 0.000 | [projects/PySnooper/verify.sh](projects/PySnooper/verify.sh) | L1 |
| 3 | [[verify.sh script]] | 0.000 | [projects/PySnooper/verify.sh](projects/PySnooper/verify.sh) | L1 |
| 4 | [[my_function()]] | 0.000 | [projects/PySnooper/verify.sh](projects/PySnooper/verify.sh) | L47 |
| 5 | [[verify.sh_1]] | 0.000 | [projects/ansible/verify.sh](projects/ansible/verify.sh) | L1 |
| 6 | [[verify.sh script_1]] | 0.000 | [projects/ansible/verify.sh](projects/ansible/verify.sh) | L1 |
| 7 | [[my_function()_1]] | 0.000 | [projects/ansible/verify.sh](projects/ansible/verify.sh) | L47 |
| 8 | [[verify.sh_2]] | 0.000 | [projects/cookiecutter/verify.sh](projects/cookiecutter/verify.sh) | L1 |
| 9 | [[verify.sh script_2]] | 0.000 | [projects/cookiecutter/verify.sh](projects/cookiecutter/verify.sh) | L1 |
| 10 | [[my_function()_2]] | 0.000 | [projects/cookiecutter/verify.sh](projects/cookiecutter/verify.sh) | L47 |
| 11 | [[verify.sh_3]] | 0.000 | [projects/keras/verify.sh](projects/keras/verify.sh) | L1 |
| 12 | [[verify.sh script_3]] | 0.000 | [projects/keras/verify.sh](projects/keras/verify.sh) | L1 |
| 13 | [[my_function()_3]] | 0.000 | [projects/keras/verify.sh](projects/keras/verify.sh) | L47 |
| 14 | [[verify.sh_4]] | 0.000 | [projects/matplotlib/verify.sh](projects/matplotlib/verify.sh) | L1 |
| 15 | [[verify.sh script_4]] | 0.000 | [projects/matplotlib/verify.sh](projects/matplotlib/verify.sh) | L1 |
| 16 | [[my_function()_4]] | 0.000 | [projects/matplotlib/verify.sh](projects/matplotlib/verify.sh) | L47 |
| 17 | [[verify.sh_5]] | 0.000 | [projects/pandas/verify.sh](projects/pandas/verify.sh) | L1 |
| 18 | [[verify.sh script_5]] | 0.000 | [projects/pandas/verify.sh](projects/pandas/verify.sh) | L1 |
| 19 | [[my_function()_5]] | 0.000 | [projects/pandas/verify.sh](projects/pandas/verify.sh) | L47 |
| 20 | [[verify.sh_6]] | 0.000 | [projects/sanic/verify.sh](projects/sanic/verify.sh) | L1 |
| 21 | [[verify.sh script_6]] | 0.000 | [projects/sanic/verify.sh](projects/sanic/verify.sh) | L1 |
| 22 | [[my_function()_6]] | 0.000 | [projects/sanic/verify.sh](projects/sanic/verify.sh) | L47 |
| 23 | [[verify.sh_7]] | 0.000 | [projects/scrapy/verify.sh](projects/scrapy/verify.sh) | L1 |
| 24 | [[verify.sh script_7]] | 0.000 | [projects/scrapy/verify.sh](projects/scrapy/verify.sh) | L1 |
| 25 | [[my_function()_7]] | 0.000 | [projects/scrapy/verify.sh](projects/scrapy/verify.sh) | L47 |
| 26 | [[verify.sh_8]] | 0.000 | [projects/tqdm/verify.sh](projects/tqdm/verify.sh) | L1 |
| 27 | [[verify.sh script_8]] | 0.000 | [projects/tqdm/verify.sh](projects/tqdm/verify.sh) | L1 |
| 28 | [[my_function()_8]] | 0.000 | [projects/tqdm/verify.sh](projects/tqdm/verify.sh) | L47 |
| 29 | [[verify.sh_9]] | 0.000 | [projects/youtube-dl/verify.sh](projects/youtube-dl/verify.sh) | L1 |
| 30 | [[verify.sh script_9]] | 0.000 | [projects/youtube-dl/verify.sh](projects/youtube-dl/verify.sh) | L1 |
| 31 | [[my_function()_9]] | 0.000 | [projects/youtube-dl/verify.sh](projects/youtube-dl/verify.sh) | L47 |
| 32 | [[update_readme.sh]] | 0.000 | [update_readme.sh](update_readme.sh) | L1 |
| 33 | [[update_readme.sh script]] | 0.000 | [update_readme.sh](update_readme.sh) | L1 |
| 34 | [[my_function()_10]] | 0.000 | [update_readme.sh](update_readme.sh) | L15 |
| 35 | [[bugsinpy-checkout]] | 0.000 | [README.md](README.md) | None |
| 36 | [[bugsinpy-compile]] | 0.000 | [README.md](README.md) | None |
| 37 | [[bugsinpy-test]] | 0.000 | [README.md](README.md) | None |
| 38 | [[bugsinpy-info]] | 0.000 | [README.md](README.md) | None |
| 39 | [[bugsinpy-coverage]] | 0.000 | [README.md](README.md) | None |
| 40 | [[bugsinpy-mutation]] | 0.000 | [README.md](README.md) | None |
| 41 | [[bugsinpy-fuzz]] | 0.000 | [README.md](README.md) | None |
| 42 | [[PySnooper Project]] | 0.000 | [projects/PySnooper/PySnooper-pass.txt](projects/PySnooper/PySnooper-pass.txt) | None |
| 43 | [[Ansible Project]] | 0.000 | [projects/ansible/ansible-pass.txt](projects/ansible/ansible-pass.txt) | None |
| 44 | [[Black Project]] | 0.000 | [projects/black/black-pass.txt](projects/black/black-pass.txt) | None |
| 45 | [[Cookiecutter Project]] | 0.000 | [projects/cookiecutter/cookiecutter-pass.txt](projects/cookiecutter/cookiecutter-pass.txt) | None |
| 46 | [[FastAPI Project]] | 0.000 | [projects/fastapi/fastapi-pass.txt](projects/fastapi/fastapi-pass.txt) | None |
| 47 | [[HTTPie Project]] | 0.000 | [projects/httpie/httpie-pass.txt](projects/httpie/httpie-pass.txt) | None |
| 48 | [[Keras Project]] | 0.000 | [projects/keras/keras-pass.txt](projects/keras/keras-pass.txt) | None |
| 49 | [[Luigi Project]] | 0.000 | [projects/luigi/luigi-pass.txt](projects/luigi/luigi-pass.txt) | None |
| 50 | [[Matplotlib Project]] | 0.000 | [projects/matplotlib/matplotlib-pass.txt](projects/matplotlib/matplotlib-pass.txt) | None |
| 51 | [[Pandas Project]] | 0.000 | [projects/pandas/pandas-pass.txt](projects/pandas/pandas-pass.txt) | None |
| 52 | [[Sanic Project]] | 0.000 | [projects/sanic/sanic-pass.txt](projects/sanic/sanic-pass.txt) | None |
| 53 | [[Scrapy Project]] | 0.000 | [projects/scrapy/scrapy-pass.txt](projects/scrapy/scrapy-pass.txt) | None |
| 54 | [[spaCy Project]] | 0.000 | [projects/spacy/spaCy-pass.txt](projects/spacy/spaCy-pass.txt) | None |
| 55 | [[TheFuck Project]] | 0.000 | [projects/thefuck/thefuck-pass.txt](projects/thefuck/thefuck-pass.txt) | None |
| 56 | [[Tornado Project]] | 0.000 | [projects/tornado/tornado-pass.txt](projects/tornado/tornado-pass.txt) | None |
| 57 | [[Tqdm Project]] | 0.000 | [projects/tqdm/tqdm-pass.txt](projects/tqdm/tqdm-pass.txt) | None |
| 58 | [[youtube-dl Project]] | 0.000 | [projects/youtube-dl/youtube-dl-pass.txt](projects/youtube-dl/youtube-dl-pass.txt) | None |
