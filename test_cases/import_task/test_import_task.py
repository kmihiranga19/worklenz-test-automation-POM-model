from page_objects.ImportTask.ImportTask import ImportTask
from page_objects.Login.login import Login
import time
from test_data.test_data import ImportTaskData
from utilities.readProperties import ReadConfig
from self import self


class TestImportTask:
    baseURL = ReadConfig.get_application_url(self)
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_import_task(self, setup):
        self.browser = setup
        self.browser.get(self.baseURL)
        self.ImportTasksData = ImportTaskData()
        self.lg = Login(self.browser)
        self.lg.enter_email()
        self.lg.setpassword(self.password)
        time.sleep(3)
        self.lg.submit()
        time.sleep(10)
        self.it = ImportTask(self.browser)
        time.sleep(3)
        self.it.clickProjectTab()
        time.sleep(3)
        self.it.selectProject()
        time.sleep(3)
        self.it.clickImportDownIcon()
        time.sleep(3)
        self.it.clickImport()
        time.sleep(3)
        self.it.clickTempInput()
        time.sleep(3)
        self.it.selectTemp()
        time.sleep(3)
        self.it.removeOneTask()
        time.sleep(3)
        self.it.clickImportBtn()
        time.sleep(5)
        self.it.clickProjectTab()
        time.sleep(3)
        self.it.clickCreateBtn()
        time.sleep(3)
        self.it.enterProjectName(self.ImportTasksData.projectName)
        time.sleep(3)
        self.it.clickProjectSubmitBtn()
        time.sleep(3)
        self.it.clickImportDownIcon()
        time.sleep(3)
        self.it.clickImport()
        time.sleep(3)
        self.it.clickTempInput()
        time.sleep(3)
        self.it.selectTemp()
        time.sleep(3)
        self.it.removeOneTask()
        time.sleep(3)
        self.it.clickImportBtn()
        time.sleep(5)
