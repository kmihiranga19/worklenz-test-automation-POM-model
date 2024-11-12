import time
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class TaskCommentsReactions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def go_task_comment_section(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space() = 'Projects']"))).click()
        t_body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        t_body_wait = WebDriverWait(t_body, 10)
        t_body_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "tr")))[0].click()
        task_row = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "worklenz-task-list-row")))[0]
        task_row_wait = WebDriverWait(task_row, 10)
        task_row_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "task-name-text"))).click()
        task_inner = task_row_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inner-task-name-container")))
        task_inner_wait = WebDriverWait(task_inner, 10)
        task_inner_wait.until(EC.visibility_of_element_located((By.TAG_NAME, "button"))).click()
        add_comment = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Add a comment...']")))
        add_comment.click()
        add_comment.send_keys("Comment 1")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Comment']"))).click()
        time.sleep(2)

    def check_whether_user_able_to_react_the_comment(self):
        comment = self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "nz-comment")))[-1]
        comment_wait = WebDriverWait(comment, 10)
        comment_wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[nztype='like']")))[-1].click()
        time.sleep(2)
        count = comment_wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "count")))[-1].text
        if int(count) == 0:
            pytest.fail("Test case fail : Check_whether_user_able_to_react_the_comment")
        else:
            pass

    def check_whether_user_able_to_react_another_member_comment(self):
        comment = self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "nz-comment")))[0]
        comment_wait = WebDriverWait(comment, 10)
        comment_wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[nztype='like']")))[-1].click()
        time.sleep(2)
        count = comment_wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "count")))[0].text
        if int(count) == 0:
            pytest.fail("Test case fail : Check_whether_user_able_to_react_another_member_comment")
        else:
            pass

    def check_whether_user_able_to_remove_reaction_on_comment(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        comment = self.wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "nz-comment")))[-1]
        comment_wait = WebDriverWait(comment, 10)
        count = comment_wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "count")))[-1].text
        if int(count) == 0:
            comment_wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[nztype='like']")))[-1].click()
            comment_wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[nztype='like']")))[-1].click()
            if int(count) > 0:
                pytest.fail("Test case fail : check_whether_user_able_to_remove_reaction_on_comment")
                
        else:
            comment_wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[nztype='like']")))[-1].click()
            if int(count) > 0:
                pytest.fail("Test case fail : check_whether_user_able_to_remove_reaction_on_comment")

    



