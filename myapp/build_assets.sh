#!/bin/bash
# Builds assets and copies them over to static/assets where Flask can serve them.
npm run build
rm -rf ../static/assets
mkdir ../static/assets
mv dist/static/css/* ../static/assets/
mv dist/static/js/* ../static/assets/
