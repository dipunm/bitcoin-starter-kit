#!/bin/fish

while :; 
    echo "refreshing..."
    pandoc title.txt **/*.md --toc -o hey.pdf --filter pandoc-crossref;
    echo "complete."
    sleep 20;
end;

