from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pyautogui
from page_objects.BasePage import Basepage
from page_objects.Locators import TaskInfoLocators


class TaskInfo(Basepage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = TaskInfoLocators()

    def clickProjectTab(self):
        self.element_click("project_tab_xpath", self.locators.project_tab_xpath)

    def selectProject(self):
        self.element_click("select_project_xpath", self.locators.select_project_xpath)

    def clickOpen(self):
        actions = ActionChains(self.browser)
        task = self.browser.find_element(By.XPATH, self.locators.div_taskName_xpath)
        actions.move_to_element(task).perform()
        time.sleep(2)
        self.browser.find_element(By.XPATH, self.locators.button_open_xpath).click()

    def clickAssignMembers(self):
        self.element_click("assignees_css", self.locators.assignees_css)

    def enterAssignName(self, assigner):
        self.enter_input_name(assigner, "assign_search_by_name_xpath", self.locators.assign_search_by_name_xpath)

    def selectAssignMember(self):
        self.element_click("member_assign_xpath", self.locators.member_assign_xpath)

    def clickTemp(self):
        self.element_click("temp_click_xpath", self.locators.temp_click_xpath)

    def clickShowStartDate(self):
        self.element_click("show_start_date_xpath", self.locators.show_start_date_xpath)

    def clickStartDate(self):
        self.element_click("start_date_xpath", self.locators.start_date_xpath)

    def setStartDate(self):
        self.element_click("start_date_select_date_css", self.locators.start_date_select_date_css)

    def clickEndDate(self):
        self.element_click("end_date_xpath", self.locators.end_date_xpath)

    def setEndDate(self):
        self.element_click("end_date_select_date_xpath", self.locators.end_date_select_date_xpath)

    def clickHideStateDate(self):
        self.element_click("hide_start_date_xpath", self.locators.hide_start_date_xpath)

    def setHours(self, hour):
        self.set_timelog(hour, "time_hours_xpath", self.locators.time_hours_xpath)

    def setMinutes(self, Minutes):
        self.set_timelog(Minutes, "time_minutes_xpath", self.locators.time_minutes_xpath)

    def clickPriority(self):
        self.element_click("priority_xpath", self.locators.priority_xpath)

    def selectHighPriority(self):
        self.element_click("high_priority_xpath", self.locators.high_priority_xpath)

    def clickLabels(self):
        self.element_click("labels_xpath", self.locators.labels_xpath)

    def createLabel(self, labelName):
        self.enter_input_name(labelName, "create_label_xpath", self.locators.create_label_xpath)

    def clickNotify(self):
        self.element_click("done_notify_css", self.locators.done_notify_css)

    def enterNotifyMember(self, notifyMember):
        self.enter_input_name(notifyMember, "notify_search_by_name_xpath", self.locators.notify_search_by_name_xpath)

    def selectNotifyMember(self):
        self.element_click("notify_member_select_xpath", self.locators.notify_member_select_xpath)

    def enterDescription(self):
        self.element_click("description_xpath", self.locators.description_xpath)

    def clickDescriptionParagraph(self):
        self.element_click("description_paragraph_xpath", self.locators.description_paragraph_xpath)

    def selectDescriptionHeading2(self):
        self.element_click("description_heading2_xpath", self.locators.description_heading2_xpath)

    def clickDescriptionNumbersList(self):
        self.element_click("description_numbersList_xpath", self.locators.description_numbersList_xpath)

    def clickDescriptionBulatList(self):
        self.element_click("description_bulatList_xpath", self.locators.description_bulatList_xpath)

    def clickDescriptionEditLink(self):
        self.element_click("description_editLink_xpath", self.locators.description_editLink_xpath)

    def enterURLEditLink(self, URL):
        self.enter_description_link(URL, "description_editLink_URL_xpath", self.locators.description_editLink_URL_xpath)

    def enterTextDisplay(self, displayText):
        self.enter_description_link(displayText, "description_editLink_TextDisplay_id",
                                    self.locators.description_editLink_TextDisplay_id)

    def enterTitleEditLink(self, title):
        self.enter_input_name(title, "description_editLink_Title_xpath", self.locators.description_editLink_Title_xpath)

    def clickOpenLinkDropDown(self):
        self.element_click("description_editLink_openLinkDw_xpath", self.locators.description_editLink_openLinkDw_xpath)

    def selectOpenLinkDropDown(self):
        self.element_click("description_editLink_openLinkSelected_xpath",
                           self.locators.description_editLink_openLinkSelected_xpath)

    def saveOpenLink(self):
        self.element_click("description_editLink_save_xpath", self.locators.description_editLink_save_xpath)

    def clickBold(self):
        self.element_click("description_Bold_xpath", self.locators.description_Bold_xpath)

    def clickItalian(self):
        self.element_click("description_italic_xpath", self.locators.description_italic_xpath)

    def clickUnderline(self):
        self.element_click("description_underline_xpath", self.locators.description_underline_xpath)

    def clickStrikethrough(self):
        self.element_click("description_Strikethrough_xpath", self.locators.description_Strikethrough_xpath)

    def clickAlignLeft(self):
        self.element_click("description_editLink_AlignLeft_xpath", self.locators.description_editLink_AlignLeft_xpath)

    def clickCenter(self):
        self.element_click("description_editLink_AlignCenter_xpath",
                           self.locators.description_editLink_AlignCenter_xpath)

    def clickAlignRight(self):
        self.element_click("description_editLink_AlignRight_xpath", self.locators.description_editLink_AlignRight_xpath)

    def clickJustify(self):
        self.element_click("description_editLink_justify_xpath", self.locators.description_editLink_justify_xpath)

    def closeDescription(self):
        self.element_click("closeDescription_xpath", self.locators.closeDescription_xpath)

    def clickLink(self):
        self.element_click("clickLink_xpath", self.locators.clickLink_xpath)

    def clickRefreshBtn(self):
        self.element_click("sub_task_refreshBtn_xpath", self.locators.sub_task_refreshBtn_xpath)

    def clickSubtask(self):
        self.element_click("add_sub_taskBtn_xpath", self.locators.add_sub_taskBtn_xpath)

    def enterSubTask(self, subTask):
        self.enter_subTask(subTask, "type_sub_taskInput_xpath", self.locators.type_sub_taskInput_xpath)

    def clickPty(self):
        self.element_click("sub_task_priority_xpath", self.locators.sub_task_priority_xpath)

    def clickPtyDropDown(self):
        self.element_click("sub_task_clickChange_priority_xpath", self.locators.sub_task_clickChange_priority_xpath)

    def selectPryDropDown(self):
        self.element_click("sub_task_select_priority_xpath", self.locators.sub_task_select_priority_xpath)

    def clickBack(self):
        self.element_click("back_btn_xpath", self.locators.back_btn_xpath)

    def clickStatus(self):
        self.element_click("sub_task_status_xpath", self.locators.sub_task_status_xpath)

    def clickStatusDropDown(self):
        self.element_click("sub_task_clickChange_status_xpath", self.locators.sub_task_clickChange_status_xpath)

    def clickAssigner(self):
        self.element_click("sub_task_assign_xpath", self.locators.sub_task_assign_xpath)

    def clickAssignerIcon(self):
        self.element_click("sub_task_clickAssign_xpath", self.locators.sub_task_clickAssign_xpath)

    def selectAssigner(self):
        self.element_click("sub_task_selectAssign_xpath", self.locators.sub_task_selectAssign_xpath)

    def clickSubTaskEditBtn(self):
        self.element_click("sub_task_editBtn_xpath", self.locators.sub_task_editBtn_xpath)

    def clickSubTaskDeleteBtn(self):
        self.element_click("sub_task_deleteBtn_css", self.locators.sub_task_deleteBtn_css)

    def selectImage(self):
        self.element_click("button_chooseImage_xpath", self.locators.button_chooseImage_xpath)
        time.sleep(3)
        # Set the file path of the AutoIT script
        autoit_script = "C:\\Users\\Ceydigital\\Pictures\\Screenshots\\Screenshot (70).PNG"
        time.sleep(1)
        pyautogui.typewrite(autoit_script)
        pyautogui.press("enter")

    def enterComment(self, comment):
        self.enter_input_name(comment, "comments_input_xpath", self.locators.comments_input_xpath)

    def submitComments(self):
        self.element_click("comments_submit_btn_xpath", self.locators.comments_submit_btn_xpath)

    def deleteComment(self):
        self.element_click("delete_comment_xpath", self.locators.delete_comment_xpath)

    def deleteOkBtn(self):
        self.element_click("ok_btn_xpath", self.locators.ok_btn_xpath)
