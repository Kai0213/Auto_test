執行 測試腳本並將測試結果存在目錄【allure-results】
pytest ./tests/test_homepage.py --alluredir=./allure-results --html=./report.html

執行generate_allure_report.py，產生可單獨開啟的測試報告，存放在目錄【allure-report】
python generate_allure_report.py


程式碼結構
AutoTest
├── allure-results          -- 存放測試結果
├── pages                   -- 頁面物件
├── logs                    -- 存放 log
├── testcase                -- 測試案例
    ├── conftest.py         -- 共用pytest fixture
    ├── test_homepage.py    -- pchome 首頁測試案例
├── utils                   -- 共用函式庫
