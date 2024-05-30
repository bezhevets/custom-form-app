This custom registration form, forked from https://github.com/open-craft/custom-form-app ,and modifed for Tutor Open edX. It works with Python3 and Open edX Koa.
You can add new fields to your register form, and download all information from the Django admin site as a CSV file.

Please test it before using in production!


## Installation on tutor:

### app installation:

`cd .local/share/tutor/env/build/openedx/requirements   `

`git clone  https://github.com/murat-polat/custom-form-app `

`echo "-e ./custom-form-app" >>  private.txt `

`pip3 install -e custom-form-app `


### plugin activation:

`tutor plugins printroot  `

`mkdir "$(tutor plugins printroot)" `

`cd "$(tutor plugins printroot)" `

`nano custom_form_plugin.yml ` Then copy all cods from custom_form_plugin.yml and save

`tutor plugins list `

`tutor plugins enable custom_form_plugin `

`tutor config save `

`tutor images build openedx  `

`tutor local quickstart `

If all done right you should see the migrations after ` tutor local quickstart `


### Debug and development:

```
tutor local run lms bash
```

```
./manage.py lms makemigrations custom_reg_form
```
```
./manage.py lms migrate
```

To delete and recreate migrations:


```
./manage.py lms migrate custom_reg_form zero
```

Than

```
./manage.py lms makemigrations custom_reg_form
```
```
./manage.py lms migrate
```