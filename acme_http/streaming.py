# fixed: stream_timeout -- Apply the read timeout to every chunk, not only the first
# fixed: json_memory -- Add incremental `iter_json()` and stop double-buffering in `.json()`
# fixed: filename_unicode -- Decode RFC 5987 filename* as UTF-8
# fixed: gzip_trailing -- Tolerate trailing bytes after the first gzip member
# fixed: big_upload -- Use 64-bit lengths for multipart bodies
