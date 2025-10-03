# Tika Demo

Ứng dụng web Flask demo trích xuất nội dung và metadata file qua Apache Tika Server.

## Hướng dẫn chạy local

1. **Cài đặt Python 3.11+ và Java (JRE/JDK)**
2. **Cài đặt thư viện Python**
   ```bash
   pip install flask requests gunicorn
   ```
3. **Tải Tika server**
   - Tải file [`tika-server-standard-3.2.2.jar`](https://dlcdn.apache.org/tika/3.2.2/tika-server-standard-3.2.2.jar)
4. **Chạy Tika server**
   ```bash
   java -jar tika-server-standard-3.2.2.jar
   ```
5. **Chạy Flask app**
   ```bash
   python app.py
   ```
6. **Truy cập giao diện web**
   - Mở trình duyệt tới [http://localhost:5000](http://localhost:5000)
   - Upload file và xem kết quả

## Ghi chú

- Tika server cần chạy trước Flask app.
