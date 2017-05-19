FILE=links.txt

while read CMD; do
    echo "$CMD"
    blc "$CMD" | grep "BROKEN" | grep -v "HTTP_403"
done < "$FILE"