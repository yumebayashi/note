git add .;
git commit -m 'add article';
git push origin master -f;
make publish;
ghp-import output;
git push origin gh-pages:gh-pages -f;
