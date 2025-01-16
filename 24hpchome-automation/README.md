執行 測試腳本並將測試結果存在目錄【allure-results】
pytest ./tests/test_homepage.py --alluredir=./allure-results --html=./report.html

執行generate_allure_report.py，產生可單獨開啟的測試報告，存放在目錄【allure-report】
python generate_allure_report.py
