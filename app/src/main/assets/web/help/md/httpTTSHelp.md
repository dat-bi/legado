# Giải thích quy tắc đọc to trực tuyến

- Quy tắc đọc to trực tuyến là quy tắc url, giống như url nguồn sách
- Tham số js

```
speakText //Văn bản đọc to
speakSpeed //Tốc độ đọc to,5-50
```

- Ví dụ:

```
http://tts.baidu.com/text2audio,{
    "method": "POST",
    "body": "tex={{java.encodeURI(java.encodeURI(speakText))}}&spd={{String((speakSpeed + 5) / 10 + 4)}}&per=5003&cuid=baidu_speech_demo&idx=1&cod=2&lan=zh&ctp=1&pdt=1&vol=5&pit=5&_res_tag_=audio"
}
```
