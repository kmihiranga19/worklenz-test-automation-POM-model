import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ImportingTemplate:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.wlTmpInitialStatuses = ["To Do", "Doing", "Done"]
        self.wlTmpInitialPriorities = ["Low", "Medium", "High"]
        self.wlTmpInitialPhases = []
        self.wlTmpInitialTasks = []
        self.wlTmpInitialLabels = []

    def go_to_projects(self):
        self.driver.get("https://uat.app.worklenz.com/worklenz/projects")
        time.sleep(10)

    def go_to_project_temp(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,
                                                          "//button[@class='ant-btn ant-dropdown-trigger ant-btn-primary ant-btn-icon-only ng-star-inserted']"))).click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@class='ant-dropdown-menu-item']"))).click()
        time.sleep(1)

    def get_need_temp(self):
        wlTemplatesList = self.driver.find_element(By.CLASS_NAME, "side-menu")
        wlTemplates = wlTemplatesList.find_elements(By.TAG_NAME, "li")
        wlTemplates[2].click()
        time.sleep(10)

    def get_description_data(self):
        description = self.driver.find_element(By.CLASS_NAME, "worklenz_value_sec")
        descriptionText = description.text
        if len(descriptionText) > 0:
            print(" description is success")

    def get_template_phase_data(self):
        phasesMenu_ = self.driver.find_element(By.CSS_SELECTOR,
                                               "div[class='cdk-global-overlay-wrapper'] div:nth-child(3) div:nth-child(2)")
        phases = phasesMenu_.find_elements(By.TAG_NAME, "nz-tag")
        for phase in phases:
            self.wlTmpInitialPhases.append(phase.text.strip())
        print("************** Start : Template phases *******************")
        print(self.wlTmpInitialPhases)
        print("************** End : Template phases ******************")

    def get_template_label_data(self):
        labelsMenu = self.driver.find_element(By.CSS_SELECTOR,
                                              "div[class='cdk-global-overlay-wrapper'] div:nth-child(6) div:nth-child(2)")
        labels = labelsMenu.find_elements(By.TAG_NAME, "nz-tag")
        for label in labels:
            self.wlTmpInitialLabels.append(label.text)
        print("************** Start : Template Labels *******************")
        print(self.wlTmpInitialLabels)
        print("************** End : Template Labels ******************")

    def get_template_tasks_data(self):
        tasksMenu = self.driver.find_element(By.CSS_SELECTOR, ".ant-list-items.ng-star-inserted")
        tasks = tasksMenu.find_elements(By.TAG_NAME, "li")
        # wlTmpInitialTasks.append(tasks)
        for task in tasks:
            self.wlTmpInitialTasks.append(task.text)
        print("************** Start : Template Tasks *******************")
        print(self.wlTmpInitialTasks)
        print("************** End : Template Tasks ******************")

    def get_template_data(self):
        self.get_description_data()
        self.get_template_phase_data()
        self.get_template_label_data()
        self.get_template_tasks_data()

    def check_tasks_data(self):
        taskListTasks = self.driver.find_elements(By.CLASS_NAME, "task-name-text")
        print(len(taskListTasks))
        print(len(self.wlTmpInitialTasks))
        if len(taskListTasks) == len(self.wlTmpInitialTasks):
            for taskListTask in taskListTasks:
                if taskListTask.text.strip() in self.wlTmpInitialTasks:
                    print("Suceesfully added ", taskListTask.text, "Task")
                if taskListTask.text.strip() not in self.wlTmpInitialTasks:
                    print("Not addded", taskListTask.text)
        else:
            print("Tasks not import correctly")

    def check_statues_data(self):
        statusesMenus = self.driver.find_elements(By.TAG_NAME, "worklenz-task-list-group-settings")
        for statusesMenu in statusesMenus:
            statusesButton = statusesMenu.find_elements(By.TAG_NAME, "button")[0]
            statuses = statusesButton.find_elements(By.TAG_NAME, "span")[1]

            if statuses.text.strip() in self.wlTmpInitialStatuses:
                print("Successfully added", statuses.text, "Status")

            if statuses.text.strip() not in self.wlTmpInitialStatuses:
                print("Not added", statuses.text, "Status")

    def check_labels_data(self):
        table_rows = self.driver.find_elements(By.TAG_NAME, "worklenz-task-list-row")
        for table_row in table_rows:
            cellsLabel = table_row.find_element(By.TAG_NAME, "worklenz-task-list-labels")
            cellsLabel.click()
            time.sleep(3)
            items = self.driver.find_elements(By.TAG_NAME, "li")
            for item in items:
                item_class_name = item.get_attribute("class")
                included_class_name = r'\bant-checkbox-wrapper-checked\b'
                check_label_class_name = re.search(included_class_name, item_class_name)
                if check_label_class_name:
                    label = item.find_element(By.CLASS_NAME, "ant-badge-status-text")
                    if label.text in self.wlTmpInitialLabels:
                        print("Successfully added ", label.text, "Label")
                    else:
                        print("Not added", label.text, "Label")
                    time.sleep(3)
            temp = self.driver.find_element(By.XPATH, "//label[normalize-space()='Group by:']")
            temp.click()
            time.sleep(3)

    def check_priorities_data(self):
        buttonsList = self.driver.find_element(By.CLASS_NAME, "ant-col")
        groupByBtn = buttonsList.find_elements(By.TAG_NAME, "button")[5]
        groupByBtn.click()
        time.sleep(1)
        dropDownMain = self.driver.find_elements(By.CLASS_NAME, "cdk-overlay-pane")[-1]
        dropDownMenu = dropDownMain.find_element(By.CLASS_NAME, "ant-dropdown-menu")
        dropDownItems = dropDownMenu.find_elements(By.TAG_NAME, "li")[1]
        dropDownItems.click()
        time.sleep(2)

        priorityMenus = self.driver.find_elements(By.TAG_NAME, "worklenz-task-list-group-settings")
        for priorityMenu in priorityMenus:
            priorityButton = priorityMenu.find_elements(By.TAG_NAME, "button")[0]
            priorities = priorityButton.find_elements(By.TAG_NAME, "span")[1]
            prioritiesFullText = priorities.text
            prioritiesOnlyText = re.sub(r'\(\d+\)', '', prioritiesFullText).strip()

            if prioritiesOnlyText in self.wlTmpInitialPriorities:
                print("Successfully added ", prioritiesOnlyText, "Priority")

            else:
                print("Not added", prioritiesOnlyText, "Priority")

    def check_phases_data(self):
        buttonsList = self.driver.find_element(By.CLASS_NAME, "ant-col")
        groupByBtn = buttonsList.find_elements(By.TAG_NAME, "button")[5]
        groupByBtn.click()
        time.sleep(1)
        dropDownMain = self.driver.find_elements(By.CLASS_NAME, "cdk-overlay-pane")[-1]
        dropDownMenu = dropDownMain.find_element(By.CLASS_NAME, "ant-dropdown-menu")
        dropDownItems = dropDownMenu.find_elements(By.TAG_NAME, "li")[2]
        dropDownItems.click()
        time.sleep(2)

        extractedPriorityText = []

        phaseMenus = self.driver.find_elements(By.TAG_NAME, "worklenz-task-list-group-settings")
        for phaseMenu in phaseMenus:
            phaseButton = phaseMenu.find_elements(By.TAG_NAME, "button")[0]
            phases = phaseButton.find_elements(By.TAG_NAME, "span")[1]
            fullText = phases.text.strip()

            onlyText = re.sub(r'\(\d+\)', '', fullText).strip()
            if onlyText in self.wlTmpInitialPhases:
                print("Succesully added ", onlyText, "Phase")

            else:
                print("Not added ", onlyText, "Phase")

    def check_data_import_correctly(self):
        self.check_tasks_data()
        self.check_statues_data()
        self.check_labels_data()
        self.check_priorities_data()
        self.check_phases_data()
