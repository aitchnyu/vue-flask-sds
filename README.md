# Use Vue with your favorite framework

This is a demonstration of using Vue.js with Flask, a Python microframework. Vue provides convenient hot-reload server which is a huge increase in productivity, but may not play nicely with your favorite framework.

## Prerequisites
```
sudo apt install python3-pip
pip3 install flask

sudo apt install nodejs npm
sudo npm install -g vue-cli
```

Install Vue.js devtools extension in your browser.

## Exploring the app
```
FLASK_APP=app.py FLASK_DEBUG=1 flask run
```

Then open the browser and visit:
```
http://127.0.0.1:5000/api
http://127.0.0.1:5000/anyotherurl
```

## Start a new Vue project
Vue CLI provides an interactive CLI which sets up a project as per your preferences and then instructions to run it.

I preferred to select no for all options.

```
vue init webpack myapp
cd myapp
npm install
npm run dev
```

This will open a new browser tab in `http://localhost:8080/`. The contents are from `myapp/src/compoenents/HelloWorld.vue`.

You may explore the hot reloading and interacting with the app state.

## Set Vue to play nicely with Flask
Implement https://github.com/vuejs-templates/webpack/issues/546#issuecomment-301357523

Also `autoOpenBrowser: false` in config/index.js

Now Flask can serve Vue apps.

I've included HelloWorld.vue for as an example in interacting with the API.

To build assets for production, run the build_assets in myapp. It will copy files over to `static/assets`. Flask picks up actual filenames using the `assets()` function. That function is cached for saving time.

