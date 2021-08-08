## Indie Coder Back-End
[![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl.svg?v=103)](https://opensource.org/licenses/GPL-3.0/)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](https://www.firsttimersonly.com/)

---
### Tools:
- Django
- Python

---

### Developer Setup:
- Fork this repository, and cd into it.
```bash
git clone https://github.com/<username>/api.git
cd api/
```

---
##### if you are using pip 
- Create and activate your virtual environment.
    - MacOS/Linux:
    ```bash
    virtualenv --no-site-packages env
    source env/bin/activate
    ```
    - Windows:
    ```
    virtualenv env
    .\env\Scripts\activate
    ```
- Install requisite python packages and modules.
```bash
pip install -r requirements.txt
```

---
##### if you are using pipenv
- Create and activate your virtual environment.
    - run
    ```bash
    pipenv shell
    ```
    ```bash
    pipenv install
    ```

---
- Verify if the Django project is working by running the development server.
```bash
python manage.py migrate
```
```bash
python manage.py runserver
```
