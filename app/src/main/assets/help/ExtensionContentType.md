```java
public enum MimeTypeEnum {

    AAC("acc", "AAC âm tần ", "audio/aac"),

    ABW("abw", "AbiWord văn kiện ", "application/x-abiword"),

    ARC("arc", " Lưu trữ văn kiện ", "application/x-freearc"),

    AVI("avi", " Âm tần video giao thoa cách thức ", "video/x-msvideo"),

    AZW("azw", " Amazon Kindle sách điện tử cách thức ", "application/vnd.amazon.ebook"),

    BIN("bin", " Bất luận cái gì loại hình số nhị phân số liệu ", "application/octet-stream"),

    BMP("bmp", "Windows OS / 2 vị đồ đồ hình ", "image/bmp"),

    BZ("bz", "BZip lưu trữ ", "application/x-bzip"),

    BZ2("bz2", "BZip2 lưu trữ ", "application/x-bzip2"),

    CSH("csh", "C-Shell kịch bản gốc ", "application/x-csh"),

    CSS("css", " Cấp liên kiểu dáng bày tỏ (CSS)", "text/css"),

    CSV("csv", " Dấu phẩy ngăn cách giá trị (CSV)", "text/csv"),

    DOC("doc", " Hơi mềm Word văn kiện ", "application/msword"),

    DOCX("docx", "Microsoft Word（OpenXML）", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),

    EOT("eot", "MS Embedded OpenType kiểu chữ ", "application/vnd.ms-fontobject"),

    EPUB("epub", " Điện tử ấn phẩm (EPUB)", "application/epub+zip"),

    GZ("gz", "GZip áp súc hồ sơ ", "application/gzip"),

    GIF("gif", " Đồ hình trao đổi cách thức (GIF)", "image/gif"),

    HTM("htm", " Siêu văn bản tiêu ký ngôn ngữ (HTML)", "text/html"),

    HTML("html", " Siêu văn bản tiêu ký ngôn ngữ (HTML)", "text/html"),

    ICO("ico", " Ô biểu tượng cách thức ", "image/vnd.microsoft.icon"),

    ICS("ics", "iCalendar cách thức ", "text/calendar"),

    JAR("jar", "Java lưu trữ ", "application/java-archive"),

    JPEG("jpeg", "JPEG hình ảnh ", "image/jpeg"),

    JPG("jpg", "JPEG hình ảnh ", "image/jpeg"),

    JS("js", "JavaScript", "text/javascript"),

    JSON("json", "JSON cách thức ", "application/json"),

    JSONLD("jsonld", "JSON-LD cách thức ", "application/ld+json"),

    MID("mid", " Nhạc khí con số tiếp lời (MIDI)", "audio/midi"),

    MIDI("midi", " Nhạc khí con số tiếp lời (MIDI)", "audio/midi"),

    MJS("mjs", "JavaScript module ", "text/javascript"),

    MP3("mp3", "MP3 âm tần ", "audio/mpeg"),

    MPEG("mpeg", "MPEG video ", "video/mpeg"),

    MPKG("mpkg", " Quả táo lắp đặt chương trình bao ", "application/vnd.apple.installer+xml"),

    ODP("odp", "OpenDocument biểu thị bản thảo văn kiện ", "application/vnd.oasis.opendocument.presentation"),

    ODS("ods", "OpenDocument bảng tính điện tử văn kiện ", "application/vnd.oasis.opendocument.spreadsheet"),

    ODT("odt", "OpenDocument văn tự văn kiện ", "application/vnd.oasis.opendocument.text"),

    OGA("oga", "OGG tin tức ", "audio/ogg"),

    OGV("ogv", "OGG video ", "video/ogg"),

    OGX("ogx", "OGG", "application/ogg"),

    OPUS("opus", "OPUS âm tần ", "audio/opus"),

    OTF("otf", "otf kiểu chữ ", "font/otf"),

    PNG("png", " Dạng đơn giản internet đồ hình ", "image/png"),

    PDF("pdf", "Adobe có thể cấy ghép văn kiện cách thức (PDF)", "application/pdf"),

    PHP("php", "php", "application/x-httpd-php"),

    PPT("ppt", "Microsoft PowerPoint", "application/vnd.ms-powerpoint"),

    PPTX("pptx", "Microsoft PowerPoint（OpenXML）", "application/vnd.openxmlformats-officedocument.presentationml.presentation"),

    RAR("rar", "RAR hồ sơ ", "application/vnd.rar"),

    RTF("rtf", " Giàu văn bản cách thức ", "application/rtf"),

    SH("sh", "Bourne Shell kịch bản gốc ", "application/x-sh"),

    SVG("svg", " Có thể thu phóng vectơ đồ hình (SVG)", "image/svg+xml"),

    SWF("swf", " Cỡ nhỏ Web cách thức (SWF) hoặc Adobe Flash văn kiện ", "application/x-shockwave-flash"),

    TAR("tar", " Băng nhạc lưu trữ (TAR)", "application/x-tar"),

    TIF("tif", " Tiêu ký hình ảnh loại văn bản (TIFF)", "image/tiff"),

    TIFF("tiff", " Tiêu ký hình ảnh loại văn bản (TIFF)", "image/tiff"),

    TS("ts", "MPEG truyền thâu lưu ", "video/mp2t"),

    TTF("ttf", "ttf kiểu chữ ", "font/ttf"),

    TXT("txt", " Văn bản ( Bình thường vì ASCII hoặc ISO 8859- n", "text/plain"),

    VSD("vsd", " Hơi mềm Visio", "application/vnd.visio"),

    WAV("wav", " Hình sóng âm tần cách thức ", "audio/wav"),

    WEBA("weba", "WEBM âm tần ", "audio/webm"),

    WEBM("webm", "WEBM video ", "video/webm"),

    WEBP("webp", "WEBP hình ảnh ", "image/webp"),

    WOFF("woff", "Web khai phóng kiểu chữ cách thức (WOFF)", "font/woff"),

    WOFF2("woff2", "Web khai phóng kiểu chữ cách thức (WOFF)", "font/woff2"),

    XHTML("xhtml", "XHTML", "application/xhtml+xml"),

    XLS("xls", " Hơi mềm Excel", "application/vnd.ms-excel"),

    XLSX("xlsx", " Hơi mềm Excel(OpenXML)", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"),

    XML("xml", "XML", "application/xml"),

    XUL("xul", "XUL", "application/vnd.mozilla.xul+xml"),

    ZIP("zip", "ZIP", "application/zip"),

    MIME_3GP("3gp", "3GPP audio/video container", "video/3gpp"),

    MIME_3GP_WITHOUT_VIDEO("3gp", "3GPP audio/video container doesn't contain video", "audio/3gpp2"),

    MIME_3G2("3g2", "3GPP2 audio/video container", "video/3gpp2"),

    MIME_3G2_WITHOUT_VIDEO("3g2", "3GPP2 audio/video container  doesn't contain video", "audio/3gpp2"),

    MIME_7Z("7z", "7-zip lưu trữ ", "application/x-7z-compressed")
}
```
