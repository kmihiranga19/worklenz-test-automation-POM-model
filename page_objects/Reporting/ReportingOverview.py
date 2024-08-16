import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import moment


class ReportingOverview:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.team_indexes = []
        self.total_projects_count = []
        self.teams_members = []
        self.teams_details = []  # type team
        self.Active_projects = []
        self.OverDue_projects = []

    def go_to_reporting(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Reporting']"))).click()
        time.sleep(10)

    def go_to_settings_team_members(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//li[5]"))).click()
        profile_details = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "profile-details-dropdown")))
        profile_details_wait = WebDriverWait(profile_details, 10)
        profile_details_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "li")))[1].click()
        time.sleep(2)
        sider = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "nz-sider")))
        sider_wait = WebDriverWait(sider, 10)
        sider.find_elements(By.TAG_NAME, "li")[8].click()
        time.sleep(2)
        pagination = self.driver.find_element(By.TAG_NAME, "nz-pagination")
        page_drop_down = pagination.find_elements(By.TAG_NAME, "li")[-1]
        page_drop_down.click()
        self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "nz-option-item")))[-1].click()
        time.sleep(3)

    def get_team_members(self):
        table = self.driver.find_element(By.TAG_NAME, "table")
        tbody = table.find_element(By.TAG_NAME, "tbody")
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cell = row.find_elements(By.TAG_NAME, "td")[2]
            teams_member = cell.text.strip()
            if teams_member not in self.teams_members:
                self.teams_members.append(teams_member)

    def get_project_end_date(self):
        end_date = self.driver.find_element(By.XPATH,
                                            "//div[2]/nz-form-item/nz-form-control/div/div/nz-date-picker/div/input")
        end_date_value = end_date.get_attribute("value")
        if end_date_value == "":
            print("not end date")
        else:
            print(end_date_value)

        drawer_close = self.driver.find_element(By.XPATH,
                                                "//div[@class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']")
        drawer_close.click()
        time.sleep(3)
        return end_date_value

    def open_team_selection(self):
        header = self.driver.find_element(By.TAG_NAME, "worklenz-header")
        header_2 = header.find_element(By.CLASS_NAME, "top-nav-ul-secondary")
        team_selection = header_2.find_elements(By.TAG_NAME, "li")[1]
        team_selection.click()
        time.sleep(5)

    def get_owner_you_team(self):
        ul = self.driver.find_element(By.CLASS_NAME, "members-dropdown")
        teams = ul.find_elements(By.TAG_NAME, "li")
        for index, team in enumerate(teams):
            owner = team.find_element(By.TAG_NAME, "small")
            Owner_by = owner.text.strip()
            if Owner_by == "Owned by You":
                self.team_indexes.append(index)

    def pagination_count_change(self):
        pagination = self.driver.find_element(By.TAG_NAME, "nz-pagination")
        page_drop_down = pagination.find_elements(By.TAG_NAME, "li")[-1]
        page_drop_down.click()
        time.sleep(2)
        page_count = self.driver.find_elements(By.TAG_NAME, "nz-option-item")[2]
        time.sleep(1)
        page_count.click()
        time.sleep(2)

    def get_own_you_teams_project_count(self):
        i = 0
        while i < len(self.team_indexes):
            team_ = {
                "id": "",
                "name": "",
                "projects": []
            }
            ul = self.driver.find_element(By.CLASS_NAME, "members-dropdown")
            teams = ul.find_elements(By.TAG_NAME, "li")
            teams[self.team_indexes[i]].click()
            time.sleep(2)
            self.go_to_settings_team_members()
            self.get_team_members()
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//strong[normalize-space()='Projects']"))).click()
            time.sleep(6)
            try:
                self.pagination_count_change()

            except NoSuchElementException:
                print("Projects not available")

            team_["name"] = "test"
            team_["projects"] = self.get_project_details()
            self.teams_details.append(team_)
            page_header_title = self.driver.find_element(By.TAG_NAME, "nz-page-header-title")
            projects_title = page_header_title.text
            projects_count = re.search(r'\d+', projects_title).group()
            self.total_projects_count.append(projects_count)
            self.open_team_selection()
            time.sleep(1)
            i = i + 1

    def get_project_details(self):
        projects = []
        t_body = self.driver.find_element(By.TAG_NAME, "tbody")
        td_ = t_body.find_element(By.TAG_NAME, "td")
        td_class_name = td_.get_attribute("class")
        if "nz-disable-td" in td_class_name:  # projects available or not
            return projects
        else:
            rows = t_body.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                icons = row.find_element(By.TAG_NAME, "nz-space")
                settings = icons.find_elements(By.TAG_NAME, "div")[0]
                settings.click()
                time.sleep(2)
                project = {
                    "name": "",
                    "start_date": "",
                    "end_date": "",
                    "is_overdue": False
                }

                project_name = self.driver.find_element(By.XPATH, "//div/input")
                project_end_date = self.driver.find_element(By.XPATH,
                                                            "//div[2]/nz-form-item/nz-form-control/div/div/nz-date-picker/div/input")
                project_start_date = self.driver.find_element(By.XPATH,
                                                              "//div[1]/nz-form-item/nz-form-control/div/div/nz-date-picker/div/input")
                project_name_text = project_name.get_attribute("value")
                project_end_date_text = project_end_date.get_attribute("value")
                project_start_date_text = project_start_date.get_attribute("value")

                project["name"] = project_name_text
                project["start_date"] = project_start_date_text
                project["end_date"] = project_end_date_text

                if project_end_date_text.strip() == "":
                    project["is_overdue"] = False
                else:
                    project["is_overdue"] = self.check_date_is_before(project_end_date_text.strip())

                projects.append(project)
                drawer_close = self.driver.find_element(By.XPATH,
                                                        "//div[@class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']")
                drawer_close.click()

            pagination = self.driver.find_element(By.TAG_NAME, "nz-pagination")
            next_btn = pagination.find_element(By.CLASS_NAME, "ant-pagination-next")
            button = next_btn.find_element(By.TAG_NAME, "button")
            if button.is_enabled():
                next_btn.click()
                time.sleep(5)
                projects += self.get_project_details()  # combine value to array
                time.sleep(3)

            return projects

        # write code if projects not
        # write code for pagination

    def check_date_is_before(self, end_date):
        f_end_date = moment.date(end_date)
        today = moment.now()
        f_end_date_without_time = f_end_date.strftime("%Y-%m-%d")
        today_date_without_time = today.strftime("%Y-%m-%d")
        if f_end_date_without_time >= today_date_without_time:
            return False
        else:
            return True

    def get_reporting_overview_first_card_details(self):
        overview_cards = self.driver.find_element(By.TAG_NAME, "worklenz-rpt-overview-cards")
        first_card = overview_cards.find_elements(By.TAG_NAME, "nz-card")[0]
        teams_details = first_card.find_element(By.CLASS_NAME, "ant-card-meta-title")
        teams_title = teams_details.text.strip()
        teams_count_reporting = re.search(r'\d+', teams_title).group()  # get only number

        projects_card_description = first_card.find_element(By.CLASS_NAME, "ant-card-meta-description")
        projects = projects_card_description.find_elements(By.TAG_NAME, "p")[0]
        project_count_reporting = re.search(r'\d+', projects.text.strip()).group()

        members = projects_card_description.find_elements(By.TAG_NAME, "p")[1]
        members_count_reporting = re.search(r'\d+', members.text.strip()).group()

        return teams_count_reporting, project_count_reporting, members_count_reporting

    def get_active_overdue_projects_count(self):
        for team_details in self.teams_details:
            for project in team_details["projects"]:
                if project['is_overdue']:
                    self.OverDue_projects.append(project)

                else:
                    self.Active_projects.append(project)

                time.sleep(1)

    def get_reporting_active_overdue_projects_count(self):
        overview_cards = self.driver.find_element(By.TAG_NAME, "worklenz-rpt-overview-cards")
        second_card = overview_cards.find_elements(By.TAG_NAME, "nz-card")[1]
        projects_description = second_card.find_element(By.CLASS_NAME, "ant-card-meta-description")
        active_projects = projects_description.find_elements(By.TAG_NAME, "p")[0]
        active_projects_count = re.search(r'\d+', active_projects.text.strip()).group()
        overdue_projects = projects_description.find_elements(By.TAG_NAME, "p")[1]
        overdue_projects_count = re.search(r'\d+', overdue_projects.text.strip()).group()
        return active_projects_count, overdue_projects_count

    def get_reporting_overview_second_card_details(self):
        overview_cards = self.driver.find_element(By.TAG_NAME, "worklenz-rpt-overview-cards")
        second_card = overview_cards.find_elements(By.TAG_NAME, "nz-card")[1]
        projects_details = second_card.find_element(By.CLASS_NAME, "ant-card-meta-title")
        projects_title = projects_details.text.strip()
        s_card_project_count_reporting = re.search(r'\d+', projects_title).group()
        return s_card_project_count_reporting

    def check_overview_first_card(self, r_team_count, r_project_count, r_member_count):
        int_team_count = int(r_team_count)
        print("Reporting Overview team count = ", int_team_count)
        print("Your actual own teams = ", len(self.team_indexes))
        if int_team_count == len(self.team_indexes):
            print("Team count is correct")

        else:
            print("Team count is wrong")

        sum_of_projects_count = sum(int(num) for num in self.total_projects_count)
        int_project_count = int(r_project_count)
        print("Reporting Overview projects count = ", int_project_count)
        print("Your actual projects count = ", sum_of_projects_count)
        if int_project_count == sum_of_projects_count:
            print("Project count is correct")

        else:
            print("Project count is wrong")

        int_member_count = int(r_member_count)
        print("Reporting Overview members count = ", int_member_count)
        print("Your actual team members count = ", len(self.teams_members))
        if int_member_count == len(self.teams_members):

            print("Teams members count is correct")

        else:
            print("Team members count is wrong")

    def check_active_overdue_projects_count(self, active_projects_no, overdue_projects_no):
        int_active_projects_no = int(active_projects_no)
        int_overdue_projects_no = int(overdue_projects_no)

        print("Reporting Overview Active projects count = ", int_active_projects_no)
        print("Your actual Active projects count = ", len(self.Active_projects))
        if len(self.Active_projects) == int_active_projects_no:
            print("Active projects count is correct")

        else:
            print("Active projects count is wrong")

        print("Reporting Overview Overdue projects count = ", int_overdue_projects_no)
        print("Your actual Overview projects count = ", len(self.OverDue_projects))
        if len(self.OverDue_projects) == int_overdue_projects_no:
            print("Overdue projects count is correct")

        else:
            print("Overdue projects count is wrong")
