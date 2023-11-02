SELECT word, count() AS occurrences
FROM
(
    SELECT arrayFilter(x -> x != '', splitByChar(' ', replaceRegexpAll(text, '[^a-zA-Zа-яА-Я ]', ' '))) AS words
    FROM lenta_ru_news
)
ARRAY JOIN words AS word
WHERE word != ''
GROUP BY word
ORDER BY occurrences DESC
LIMIT 100