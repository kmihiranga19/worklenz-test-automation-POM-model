from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TaskList:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Project']"
    to_do_xpath = "//span[normalize-space()='To Do (0)']"
    add_task_xpath = "(//span[contains(text(),'Add Task')])[1]"
    enter_task_xpath = "//input[@placeholder='Type your task and hit enter']"
    member_assign_xpath = "//nz-avatar[@class='ant-avatar avatar-dashed bg-white ant-avatar-circle ant-avatar-icon']"
    search_member_xpath = "//input[@placeholder='Search by name']"
    select_member_xpath = "//div[@class='cdk-overlay-container']//li[2]//span[2]"
    ok_btn_xpath = "//span[normalize-space()='OK']"
    labels_xpath = "//nz-tag[@class='ant-tag text-dark avatar-dashed empty-label task-list-label']"
    create_label_xpath = "//input[@placeholder='Search or create']"
    select_label_xpath = "//li[1]//span[1]//input[1]"
    status_xpath = "//nz-select-item[normalize-space()='To Do']"
    status_doing_xpath = "//nz-option-item[@title='Doing']"
    priority_xpath = "//nz-select-item[@title='Medium']"
    priority_high_xpath = "//span[normalize-space()='High']"
    scroll_right_xpath = "(//div[@id='dd1215c8-9108-4590-a88c-6cf706324bc5'])[1]"
    time_log_start_xpath = "//span[@class='anticon anticon-caret-right ng-star-inserted']//*[name()='svg']"
    time_log_pause_xpath = "//span[@class='nz-icon icon-stop ng-star-inserted']//*[name()='svg']"
    time_log_details_xpath = "//span[normalize-space()='0m 0s']"
    due_date_xpath = "//div[@id='dd1215c8-9108-4590-a88c-6cf706324bc5']/div/worklenz-task-list-row/div/worklenz-task-list-end-date/div/nz-date-picker/div/input"
    due_date_select_xpath = "//calendar-footer/div/a"
    sub_task_xpath = "(//div[@class='flex-row task-arrow'])[3]"
    sub_task_open_xpath = "//span[normalize-space()='Add sub-task']"
    sub_task_enter_xpath = "//input[@placeholder='Type your task and hit enter']"
    sub_task_close_xpath = "//worklenz-task-list-row[1]//div[1]//div[3]//div[1]//div[1]"
    task_right_click_xpath = "//worklenz-task-list-row[1]//div[1]//div[4]//div[1]//div[1]//div[1]//div[1]//div[1]"
    assign_to_me_xpath = "//li[normalize-space()='Assign to me']"
    task_right_click = "//worklenz-task-list-row[1]//div[1]//div[4]//div[1]//div[1]//div[1]//div[1]//div[1]"
    move_to_xpath = "(//div[@class='ant-dropdown-menu-submenu-title'])[1]"
    move_to_done_xpath = "(//li[@class='m-0 ant-dropdown-menu-item ng-star-inserted'])[3]"
    scroll_down_xpath = "(//html)[1]"
    archive_select_xpath = "//li[@class='ant-dropdown-menu-item ng-star-inserted']"
    view_archivers_xpath = "//span[normalize-space()='Show archived']"
    task_right_click2_xpath = "(//div[@class='task-name-text ng-star-inserted'])[1]"
    unarchived_xpath = "(//li[@class='ant-dropdown-menu-item ng-star-inserted'])[1]"
    show_archived_xpath = "//span[normalize-space()='Show archived']"
    add_task_new_xpath = "(//span[contains(text(),'Add Task')])[3]"
    type_task_xpath = "//input[@placeholder='Type your task and hit enter']"
    task_right_click3_xpath = "(//div[@class='task-name-text ng-star-inserted'])[2]"
    convert_to_sub_task_xpath = "//li[normalize-space()='Convert to Sub task']"
    search_parent_task_xpath = "//input[@placeholder='Search by task name']"
    select_parent_task_xpath = "//span[normalize-space()='Task 01']"
    open_parent_task_xpath = "(//div[@class='p-0 border-end-0'])[1]"
    task_right_click4_xpath = "(//div[@class='task-name-text ng-star-inserted'])[2]"
    convert_to_parent_task_xpath = "(//li[@class='ant-dropdown-menu-item ng-star-inserted'])[1]"
    task_right_click5_xpath = "(//div[@class='task-name-text ng-star-inserted'])[2]"
    delete_task_xpath = "//li[normalize-space()='Delete']"
    category_dont_xpath = "(//span[@class='anticon anticon-ellipsis'])[4]"
    rename_category_xpath = "//li[@class='ant-dropdown-menu-item']"
    rename_type_xpath = "//input[@id='group-name-20743845-aef5-4428-b3d4-8b812f246f08']"
    category_change = "//div[@class='ant-dropdown-menu-submenu-title']"
    category_change_todo_xpath = "//span[@class='ng-star-inserted'][normalize-space()='Done']"
    open_have_to_do_category_xpath = "(//button[@class='ant-btn collapse btn border-0'])[3]"
    add_task1_xpath = "(//span[contains(text(),'Add Task')])[3]"
    enter_task1_xpath = "//input[@placeholder='Type your task and hit enter']"
    task_right_click6_xpath = "(//div[@class='flex-row task-arrow'])[5]"
    bottom_action_status_xpath = "//nz-select-item[@title='To Do']"
    task_right_click7_xpath = "(//div[@class='flex-row task-arrow'])[4]"
    change_label_xpath = "//span[@class='anticon anticon-tags']//*[name()='svg']"
    apply_xpath = "//span[normalize-space()='Apply']"
    task_right_click8_xpath = "(//div[@class='flex-row task-arrow'])[4]"
    task_right_click9_xpath = "(//div[@class='flex-row task-arrow'])[4]"
    archive_xpath = "//span[@class='anticon anticon-inbox']//*[name()='svg']"
    task_right_click10_xpath = "(//input[@type='checkbox'])[5]"
    show_unarchived_xpath = "//span[normalize-space()='Show archived']"
    more_option_xpath = "(//*[name()='svg'])[57]9"
    create_temp_xpath = "//span[normalize-space()='Create Task Template']"
    temp_name_xpath = "//input[@placeholder='Template Name']"
    save_btn_xpath = "//span[normalize-space()='Save']"
    task_right_click11_xpath = "(//input[@class='ant-checkbox-input ng-valid ng-dirty ng-touched'])[1]"
    task_right_click12_xpath = "(//input[@class='ant-checkbox-input ng-valid ng-dirty ng-touched'])[1]"
    delete_task2_xpath = "//div[@class='d-flex align-items-center position-relative justify-content-center']//button[@class='ant-btn ant-btn-text ant-btn-circle ant-btn-icon-only']"

    def __init__(self, browser):
        self.browser = browser

    def clickProjectTab(self):
        self.browser.find_element(By.XPATH, self.project_tab_xpath).click()

    def selectProject(self):
        self.browser.find_element(By.XPATH, self.select_project_xpath).click()

    def clickToDo(self):
        self.browser.find_element(By.XPATH, self.to_do_xpath).click()

    def clickAddTask(self):
        self.browser.find_element(By.XPATH, self.add_task_xpath).click()

    def enterTask(self, TaskName):
        self.browser.find_element(By.XPATH, self.enter_task_xpath).click()
        self.browser.find_element(By.XPATH, self.enter_task_xpath).send_keys(TaskName + Keys.ENTER)

    def clickMemberAssign(self):
        self.browser.find_element(By.XPATH, self.member_assign_xpath).click()

    def searchMember(self, searchMember):
        self.browser.find_element(By.XPATH, self.search_member_xpath).click()
        self.browser.find_element(By.XPATH, self.search_member_xpath).send_keys(searchMember)

    def selectMember(self):
        self.browser.find_element(By.XPATH, self.select_member_xpath).click()

    def clickOkButton(self):
        self.browser.find_element(By.XPATH, self.ok_btn_xpath).click()

    def clickLabel(self):
        self.browser.find_element(By.XPATH, self.labels_xpath).click()

    def createLabel(self, labelName):
        self.browser.find_element(By.XPATH, self.create_label_xpath).click()
        self.browser.find_element(By.XPATH, self.create_label_xpath).send_keys(labelName + Keys.ENTER)

    def selectLabel(self):
        self.browser.find_element(By.XPATH, self.select_label_xpath).click()

    def clickStatus(self):
        self.browser.find_element(By.XPATH, self.status_xpath).click()

    def statusDoing(self):
        self.browser.find_element(By.XPATH, self.status_doing_xpath).click()

    def clickPriority(self):
        self.browser.find_element(By.XPATH, self.priority_xpath).click()

    def priorityHigh(self):
        self.browser.find_element(By.XPATH, self.priority_high_xpath).click()

    def scroll_right(self):
        scroll_right = self.browser.find_element(By.XPATH, self.scroll_right_xpath)
        self.browser.execute_script("arguments[0].scrollBy(1000, 0);", scroll_right)

    def timeLogStart(self):
        self.browser.find_element(By.XPATH, self.time_log_start_xpath).click()

    def timeLogPause(self):
        self.browser.find_element(By.XPATH, self.time_log_pause_xpath).click()

    def timeLogDetails(self):
        self.browser.find_element(By.XPATH, self.time_log_details_xpath).click()

    def dueDate(self):
        self.browser.find_element(By.XPATH, self.due_date_xpath).click()

    def selectDueDate(self):
        self.browser.find_element(By.XPATH, self.due_date_select_xpath).click()

    def scroll_left(self):
        scroll_left = self.browser.find_element(By.XPATH, self.scroll_right_xpath)
        self.browser.execute_script("arguments[0].scrollBy(-1000, 0);", scroll_left)

    def subTask(self):
        self.browser.find_element(By.XPATH, self.sub_task_xpath).click()

    def subTaskOpen(self):
        self.browser.find_element(By.XPATH, self.sub_task_open_xpath).click()

    def subTaskEnter(self, subTaskName):
        self.browser.find_element(By.XPATH, self.sub_task_enter_xpath).send_keys(subTaskName + Keys.ENTER)

    def subTaskClose(self):
        self.browser.find_element(By.XPATH, self.sub_task_close_xpath).click()

    def taskRightClick1(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def assignToMe(self):
        self.browser.find_element(By.XPATH, self.assign_to_me_xpath).click()

    # taskRightClick1

    def moveTo(self):
        self.browser.find_element(By.XPATH, self.move_to_xpath).click()

    def moveToDone(self):
        self.browser.find_element(By.XPATH, self.move_to_done_xpath).click()

    def scrollDown(self):
        scroll_down = self.browser.find_element(By.XPATH, self.scroll_down_xpath)
        self.browser.execute_script("arguments[0].scrollBy(0, 1000);", scroll_down)

    def taskRightClick2(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click2_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def archiveSelect(self):
        self.browser.find_element(By.XPATH, self.archive_select_xpath).click()

    def viewArchives(self):
        self.browser.find_element(By.XPATH, self.view_archivers_xpath).click()

    def taskRightClick3(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click2_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def unarchived(self):
        self.browser.find_element(By.XPATH, self.unarchived_xpath).click()

    def showArchived(self):
        self.browser.find_element(By.XPATH, self.show_archived_xpath).click()

    def addTaskNew(self):
        self.browser.find_element(By.XPATH, self.add_task_new_xpath).click()

    def typeTask(self, TaskName):
        self.browser.find_element(By.XPATH, self.type_task_xpath).send_keys(TaskName + Keys.ENTER)

    def taskRightClick4(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click4_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def convertToSubTask(self):
        self.browser.find_element(By.XPATH, self.convert_to_sub_task_xpath).click()

    def searchParentTask(self, SearchParentName):
        self.browser.find_element(By.XPATH, self.search_parent_task_xpath).click()
        self.browser.find_element(By.XPATH, self.search_parent_task_xpath).send_keys(SearchParentName)

    def selectParentTask(self):
        self.browser.find_element(By.XPATH, self.select_parent_task_xpath).click()

    def openParentTask(self):
        self.browser.find_element(By.XPATH, self.open_parent_task_xpath).click()

    def taskRightClick5(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click5_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def deleteTask(self):
        self.browser.find_element(By.XPATH, self.delete_task_xpath).click()

    def categoryDont(self):
        self.browser.find_element(By.XPATH, self.category_dont_xpath).click()

    def renameCategory(self):
        self.browser.find_element(By.XPATH, self.rename_category_xpath).click()

    def renameType(self, NewCategoryName):
        self.browser.find_element(By.XPATH, self.rename_type_xpath).send_keys(
            Keys.BACKSPACE + NewCategoryName + Keys.ENTER)

    def categoryChange(self):
        self.browser.find_element(By.XPATH, self.category_change).click()

    def categoryChangeTodo(self):
        self.browser.find_element(By.XPATH, self.category_change_todo_xpath).click()

    def openHaveToDOCategory(self):
        self.browser.find_element(By.XPATH, self.open_have_to_do_category_xpath).click()

    def addTask(self):
        self.browser.find_element(By.XPATH, self.add_task1_xpath).click()

    def typeTaskN(self, TaskName):
        self.browser.find_element(By.XPATH, self.enter_task1_xpath).send_keys(TaskName + Keys.ENTER)

    def taskRightClick6(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click6_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def bottomActionStatus(self):
        self.browser.find_element(By.XPATH, self.bottom_action_status_xpath).click()

    def status_doing(self):
        self.browser.find_element(By.XPATH, self.status_doing_xpath).click()

    def taskRightClick7(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click7_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def changeLabel(self):
        self.browser.find_element(By.XPATH, self.change_label_xpath).click()

    def selectLabelN(self):
        self.browser.find_element(By.XPATH, self.select_label_xpath).click()

    def apply(self):
        self.browser.find_element(By.XPATH, self.apply_xpath).click()

    def taskRightClick8(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click8_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def assignToMeN(self):
        self.browser.find_element(By.XPATH, self.assign_to_me_xpath).click()

    def taskRightClick9(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click9_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def archive(self):
        self.browser.find_element(By.XPATH, self.archive_xpath).click()

    def showArchive(self):
        self.browser.find_element(By.XPATH, self.show_archived_xpath).click()

    def taskRightClick10(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click10_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def unArchived(self):
        self.browser.find_element(By.XPATH, self.unarchived_xpath).click()

    def showUnArchived(self):
        self.browser.find_element(By.XPATH, self.show_unarchived_xpath).click()

    def taskRightClick11(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click11_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def moreOption(self):
        self.browser.find_element(By.XPATH, self.more_option_xpath).click()

    def createTemp(self):
        self.browser.find_element(By.XPATH, self.create_temp_xpath).click()

    def tempName(self, tempTask):
        self.browser.find_element(By.XPATH, self.temp_name_xpath).click()
        self.browser.find_element(By.XPATH, self.temp_name_xpath).send_keys(tempTask + Keys.ENTER)

    def saveBtn(self):
        self.browser.find_element(By.XPATH, self.save_btn_xpath).click()

    def taskRightClick12(self):
        task_right_click = self.browser.find_element(By.XPATH, self.task_right_click12_xpath)
        actions = ActionChains(self.browser)
        actions.context_click(task_right_click).perform()

    def deleteTaskN(self):
        self.browser.find_element(By.XPATH, self.delete_task2_xpath).click()
