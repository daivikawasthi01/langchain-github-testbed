# fixed: stream_timeout -- Apply the read timeout to every chunk, not only the first
# fixed: json_memory -- Add incremental `iter_json()` and stop double-buffering in `.json()`
# fixed: filename_unicode -- Decode RFC 5987 filename* as UTF-8
# known-issue: gzip_trailing
# known-issue: big_upload
