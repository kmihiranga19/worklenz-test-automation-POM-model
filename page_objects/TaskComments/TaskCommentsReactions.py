from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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
        comment_input = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "worklenz-task-view-comments-input")))
        comment_input_wait = WebDriverWait(comment_input, 10)
        comment_input_wait.until(EC.visibility_of_element_located((By.XPATH, "textarea[placeholder='Add a comment...']"))).send_keys("Comment 1")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "button[type='submit']"))).click()

