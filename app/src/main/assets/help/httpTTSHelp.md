```
# Tại tuyến đọc chậm quy tắc chứng minh
* Tại tuyến đọc chậm quy tắc vì url quy tắc, cùng sách nguyên url
* js tham số
```
speakText // đọc chậm văn bản
speakSpeed // đọc chậm tốc độ,0-45
```
* Lệ:
```
http://tts.baidu.com/text2audio,{
"method": "POST",
"body": "tex={{java.encodeURI(java.encodeURI(speakText))}}&spd={{String((speakSpeed + 5) / 10 + 4)}}&per=5003&cuid=baidu_speech_demo&idx=1&cod=2&lan=zh&ctp=1&pdt=1&vol=5&pit=5&_res_tag_=audio"
}
```