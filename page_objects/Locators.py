# class CommonLocators:

class AdminCenterOverviewLocators:
    profile_icon_xpath = "(//li[@class='menu-hover menu-border-0 prevent-default ant-typography ant-menu-item'])[1]"
    admin_center_btn_xpath = "//li[@class='pl-def pr-def ng-star-inserted']"
    organization_name_xpath = "//p[@class='ant-typography']//span[@class='anticon anticon-edit ng-star-inserted']//*[name()='svg']"
    input_xpath = "//textarea[@class='ant-input ng-star-inserted']"
    organization_owner_xpath = "//span[@class='anticon edit-btn anticon-edit ng-star-inserted']//*[name()='svg']"
    input2_xpath = "//input[@placeholder='Add Contact Number']"


class AdminCenterTeamsLocators:
    teams_btn_xpath = "//span[normalize-space()='Teams']"
    refresh_btn_xpath = "//button[@class='ant-btn ant-btn-circle ant-btn-icon-only ng-star-inserted']"
    add_team_xpath = "//span[contains(text(),'Add Team')]"
    team_name_xpath = "//div/input"
    create_btn_xpath = "//button[@type='submit']"
    search_xpath = "//input[@placeholder='Search by name']"
    page_selector_xpath = "//nz-select-item[@title='20 / page']"
    page_5_xpath = "//nz-option-item[5]"


class AdminCenterUsersLocators:
    users_btn_xpath = "//span[normalize-space()='Users']"
    refresh_btn_xpath = "//button[@class='ant-btn ant-btn-circle ant-btn-icon-only ng-star-inserted']"
    search_xpath = "//input[@placeholder='Search by name']"
    page_selector_xpath = "//nz-select-item[@title='20 / page']"
    page5_xpath = "//nz-option-item[1]"


class CreateProjectLocators:
    new_project_button_xpath = "//span[normalize-space()='New Project']"
    create_project_xpath = "//span[contains(text(),'Create Project')]"
    name_input_xpath = "//input[@placeholder='Name']"
    project_color_xpath = "//nz-tag"
    select_project_color_xpath = "//li[5]/nz-tag"
    status_dropDown_xpath = "//nz-select-item[@title='Proposed']"
    in_progressOption_xpath = "//nz-option-item[@title='In Progress']//div[1]"
    notes_input_xpath = "//textarea[@placeholder='Notes']"
    client_input_xpath = "//input[@placeholder='Select client']"
    client_option_xpath = "//div[@class='ant-select-item-option-content']"
    start_date_xpath = "//nz-date-picker/div/input"
    select_date_xpath = "//calendar-footer/div/a"
    end_date_xpath = "//div[2]/nz-form-item/nz-form-control/div/div/nz-date-picker/div/input"
    submit_button_xpath = "//button[@type='button']//span[@class='ng-star-inserted'][normalize-space()='Create']"
    project_tab_xpath = "//strong[normalize-space()='Projects']"


class HomeBugsLocators:
    project_Tab_xpath = "//strong[normalize-space()='Projects']"
    project_select_xpath = "//span[normalize-space()='HomeTest']"
    project_group_By = "//span[normalize-space()='Status']"
    phase_xpath = "(//span[@class='ant-typography'][normalize-space()='Phase'])[1]"
    home_xpath = "//strong[normalize-space()='Home']"
    task_input_xpath = "(//input[@placeholder='+ Add Task'])[1]"
    select_today_xpath = "//div[@class='ant-select-item-option-content'][normalize-space()='Today']"
    select_project_xpath = "//div[contains(text(),'HomeTest')]"
    task_xpath = "//p[normalize-space()='Testing task']"
    open_task_xpath = "//span[normalize-space()='Open']"
    subTask_xpath = "//span[normalize-space()='Add sub-task']"
    enter_subtask_xpath = "//input[@placeholder='Type your task and hit enter']"


# HomeXpath need

class ImportTaskLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Testing kanban board']"
    import_down_icon_xpath = "//span[@class='anticon anticon-down']"
    import_task_xpath = "//li[@class='ant-dropdown-menu-item']"
    temp_input_xpath = "//nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input"
    select_temp_xpath = "//nz-option-item/div"
    remove_task_xpath = "//li[2]//ul[1]//li[1]//a[1]"
    import_btn_xpath = "//span[normalize-space()='Import']"
    create_project_xpath = "//span[contains(text(),'Create Project')]"
    project_name_xpath = "//input[@placeholder='Name']"
    create_btn_xpath = "//button[@class='ant-btn ant-btn-primary ant-btn-block ng-star-inserted']"


class SignUpLocators:
    login_btn_xpath = "//button[@class='btn worklenz_btn-login']"
    signUp_btn_xpath = "//a[normalize-space()='Sign Up']"
    enter_name_xpath = "//input[@id='full-name']"
    enter_email_xpath = "//input[@id='email']"
    enter_password_xpath = "//input[@id='password']"
    submit_xpath = "//span[normalize-space()='Sign up']"


class InviteOnboardingLocators:
    enter_organization_xpath = "//input[@type='text']"
    continue_btn1_xpath = "//span[normalize-space()='Continue']"
    enter_project_xpath = "//input[@type='text']"
    continue_btn2_xpath = "//span[normalize-space()='Continue']"
    enter_task_xpath = "//*[@id='task-name-input-0']"
    enter_inviteEmail_tag = "input"


class InviteProjectLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    create_project_btn_xpath = "//span[contains(text(),'Create Project')]"
    project_name_input_xpath = "//input[@placeholder='Name']"
    project_submit_btn_xpath = "//form/button/span"
    select_project_xpath = "//span[normalize-space()='Testing kanban board']"
    invite_btn_xpath = "//span[normalize-space()='Invite']"
    delete_project_members_xpath = "//nz-list-item[1]//button[1]//span[1]//*[name()='svg']"
    ok_btn_xpath = "//span[normalize-space()='OK']"
    enter_invite_email_xpath = "//nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input"


class InviteSettingsLocators:
    profile_icon_xpath = "(//li[@class='menu-hover menu-border-0 prevent-default ant-typography ant-menu-item'])[1]"
    settings_xpath = "//li[normalize-space()='Settings']"
    click_team_membersTab_xpath = "//span[normalize-space()='Team Members']"
    add_member_xpath = "//button[@class='ant-btn ant-btn-primary']//span[@class='ng-star-inserted'][normalize-space()='Add Member']"
    invite_member_xpath = "//div/nz-select/nz-select-top-control"
    enter_invite_member_xpath = "//div/nz-select/nz-select-top-control/nz-select-search/input"
    job_title_xpath = "//div/input"
    access_xpath = "//nz-select-item[@title='Member']"
    select_access_xpath = "//div[normalize-space()='Admin']"
    submit_btn_xpath = "//span[normalize-space()='Add to team']"


class LoginLocators:
    login_btn_xpath = "//button[@class='btn worklenz_btn-login']"
    email_input_xpath = "//input[@placeholder='Email']"
    password_input_xpath = "//input[@placeholder='Password']"
    login_submit_btn_xpath = "//button[@class='ant-btn mt-1 ant-btn-primary ant-btn-lg ant-btn-block']"


class LogOutLocators:
    profile_icon_xpath = "(//li[@class='menu-hover menu-border-0 prevent-default ant-typography ant-menu-item'])[1]"
    log_out_btn_xpath = "//li[normalize-space()='Log Out']"
    cancel_btn_xpath = "//span[normalize-space()='Cancel']"
    ok_btn_xpath = "//span[normalize-space()='OK']"


class NotificationsLocators:
    notification_icon_xpath = "(//*[name()='svg'])[3]"
    mark_as_read_xpath = "//div[@class='ant-drawer-wrapper-body']//div[1]//div[1]//div[2]//button[1]//u[1]"
    read_button_xpath = "//div[normalize-space()='Read']"
    unread_btn_xpath = "//div[normalize-space()='Unread']"
    mark_all_as_read_xpath = "//span[normalize-space()='Mark all as read']"
    join_btn_xpath = "//u[normalize-space()='Read & Join']"
    close_btn_xpath = "//div[@class='ant-drawer-content-wrapper notifications-drawer']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']"


class PhaseLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Testing phase']"
    project_group_by_xpath = "//span[normalize-space()='Status']"
    select_phase_xpath = "//span[@class='ant-typography'][normalize-space()='Phase']"
    show_filed_xpath = "//span[normalize-space()='Show fields']"
    scroll_down_xpath = "//div[10]/div/div/ul"
    select_phase_filed_xpath = "(//span[contains(text(),'Phase')])[2]"
    phase_settings_xpath = "(//span[@class='anticon anticon-setting'])[2]"
    phase_label_xpath = "//input[@id='label']"
    add_phase_option_xpath = "//span[normalize-space()='Add Option']"
    phase_option_01_xpath = "//form[2]/nz-form-item/nz-form-control/div/div/input"
    phase_option_02_xpath = "//nz-form-item[2]/nz-form-control/div/div/input"
    phase_option_03_xpath = "//nz-form-item[3]/nz-form-control/div/div/input"
    phase_option_delete_xpath = "(//label[@class='ant-form-item-no-colon'])[2]"
    close_drawer_xpath = "//div[@class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']"
    phase_menu_xpath = "(//span[@class='anticon anticon-ellipsis'])[2]"
    renameBtn_xpath = "//li[@class='ant-dropdown-menu-item']"
    renamePhase_xpath = "//button/input"
    unmapped_add_task_xpath = "(//span[contains(text(),'Add Task')])[3]"
    unmapped_enter_task_xpath = "//input[@placeholder='Type your task and hit enter']"
    planing_option_xpath = "//span[normalize-space()='Planning (0)']"
    planing_option_add_task_xpath = "//div[2]/div/div/div/div[2]/worklenz-task-list-add-task-input/div/span[2]"
    planing_option_enter_task_xpath = "//form/input"
    task_right_click_xpath = "//div/div[2]/span/span/input"
    task_move_to_xpath = "//li[2]/div"
    select_move_to_review_xpath = "//nz-badge/span[2]"
    convert_to_sub_task_xpath = "//li[contains(.,'Convert to Sub task')]"
    select_parent_task_xpath = "//li[2]/div/div[2]"
    sub_task_view_xpath = "(//div[@class='flex-row task-arrow'])[5]"
    sub_task_right_click_xpath = "//div[3]/div/div/div/div/div/div/worklenz-task-list-row/div/div[2]/span/span/input"
    convert_to_task_xpath = "//div/div/ul/li[2]"


class ProfileLocators:
    profile_icon_xpath = "(//li[@class='menu-hover menu-border-0 prevent-default ant-typography ant-menu-item'])[1]"
    admin_center_xpath = "//li[@class='pl-def pr-def ng-star-inserted']"
    profile_icon2_xpath = "(//li[@class='menu-hover menu-border-0 prevent-default ant-typography ant-menu-item ant-menu-item-selected'])[1]"
    settings_xpath = "//li[normalize-space()='Settings']"
    log_out_xpath = "//li[normalize-space()='Log Out']"
    close_btn_xpath = "//span[@class='ant-modal-close-x']"


class SettingsChangePasswordLocators:
    psw_change_xpath = "//span[normalize-space()='Change Password']"
    current_psw_xpath = "//input[@placeholder='Enter your current password']"
    view_xpath = "(//*[name()='svg'])[15]"
    hide_xpath = "(//*[name()='path'])[16]"
    new_psw_xpath = "//input[@placeholder='New Password']"
    confirm_psw_xpath = "//input[@placeholder='Confirm New Password']"
    updateBtn_xpath = "//span[normalize-space()='Update']"


class SettingsClientsLocators:
    client_tab_xpath = "//span[normalize-space()='Clients']"
    create_client_btn_xpath = "//span[normalize-space()='Create Client']"
    enter_name_xpath = "//input[@placeholder='Name']"
    create_button_xpath = "//button[@class='ant-btn ant-btn-primary ant-btn-block']"
    search_by_name_xpath = "//input[@placeholder='Search by name']"
    client_edit_btn_xpath = "//tbody/tr[1]/td[3]/div[1]/nz-space[1]/div[1]/button[1]/span[1]//*[name()='svg']"
    client_name_update_xpath = "//input[@placeholder='Name']"
    update_btn_xpath = "//button[@class='ant-btn ant-btn-primary ant-btn-block']"
    client_delete_btn_xpath = "//tbody/tr[1]/td[3]/div[1]/nz-space[1]/div[2]/button[1]/span[1]//*[name()='svg']"
    delete_yes_btn_xpath = "//span[normalize-space()='Yes']"
    pin_client_xpath = "//span[@class='anticon pin-button anticon-pushpin']//*[name()='svg']"
    unpin_xpath = "//*[name()='path' and contains(@d,'M878.3 392')]"
    page_selector_xpath = "//nz-select-item[@title='20 / page']"
    page_selector_10_xpath = "//nz-option-item[1]"


class SettingsJobTitleLocators:
    job_title_tab_xpath = "//span[normalize-space()='Job Titles']"
    client_job_title_btn_xpath = "//span[normalize-space()='Create Job Title']"
    enter_name_xpath = "//input[@placeholder='Name']"
    create_btn_xpath = "//button[@type='submit']"
    search_by_name_xpath = "//input[@placeholder='Search by name']"
    job_edit_btn_xpath = "//tbody/tr[1]/td[2]/div[1]/nz-space[1]/div[1]/button[1]/span[1]//*[name()='svg']"
    job_name_update_xpath = "//input[@placeholder='Name']"
    update_btn_xpath = "//button[@class='ant-btn ant-btn-primary ant-btn-block']"
    job_delete_btn_xpath = "//tbody/tr[1]/td[2]/div[1]/nz-space[1]/div[2]/button[1]/span[1]//*[name()='svg']"
    delete_yes_btn_xpath = "//span[normalize-space()='Yes']"
    pin_job_title_xpath = "//span[@class='anticon pin-button anticon-pushpin']//*[name()='svg']"
    unpin_job_title_xpath = "//*[name()='path' and contains(@d,'M878.3 392')]"
    page_selector_xpath = "//nz-select-item[@title='20 / page']"
    page_selector_10_xpath = "//nz-option-item[1]"


class SettingsLabelsLocators:
    label_tab_xpath = "//span[normalize-space()='Labels']"
    label_search_xpath = "//input[@placeholder='Search by name']"
    pin_labelTab_xpath = "//span[@class='anticon pin-button anticon-pushpin']//*[name()='svg']"
    unpin_labelTab_xpath = "//*[name()='path' and contains(@d,'M878.3 392')]"


class SettingsLanguageLocators:
    language_region_xpath = "//span[normalize-space()='Language & Region']"
    language_select_xpath = "//nz-select-item[@title='English']"
    english_xpath = "//div[@class='ant-select-item-option-content']"
    time_zone_xpath = "//nz-select-item[@title='Asia/Colombo']"
    select_time_zone_xpath = "//span[normalize-space()='Asia/Colombo']"
    save_btn_xpath = "//span[normalize-space()='Save Changes']"


class SettingsNotificationsLocators:
    notifications_tab_xpath = "//span[normalize-space()='Notifications']"
    email_notifications_xpath = "//h4[normalize-space()='Send me email notifications']"
    daily_digest_xpath = "//h4[normalize-space()='Send me a daily digest']"
    push_notifications_xpath = "//h4[contains(text(),'Pop up notifications on my computer when Worklenz ')]"
    unread_items_xpath = "//h4[normalize-space()='Show the number of unread items']"


class SettingsProfileLocators:
    profile_icon_xpath = "(//li[@class='menu-hover menu-border-0 prevent-default ant-typography ant-menu-item'])[1]"
    settings_xpath = "//li[normalize-space()='Settings']"
    upload_xpath = "//div[@role='button']"
    name_xpath = "//input[@id='name']"
    save_btn_xpath = "//span[normalize-space()='Save Changes']"


class SettingsTaskTemplatesLocators:
    tasks_template_tab_xpath = "//span[normalize-space()='Task Templates']"


class SettingsTeamMemberLocators:
    team_members_tab_xpath = "//span[normalize-space()='Team Members']"
    refresh_btn_xpath = "//span[@class='anticon anticon-sync']"
    search_input_xpath = "//input[@placeholder='Search by name']"
    add_member_btn_xpath = "//button[@class='ant-btn ant-btn-primary']//span[@class='ng-star-inserted'][normalize-space()='Add Member']"
    enter_email_xpath = "//div/nz-select/nz-select-top-control"
    member_edit_xpath = "//tbody/tr[1]/td[5]/div[1]/nz-space[1]/div[1]/button[1]/span[1]//*[name()='svg']"
    job_title_xpath = "//input[@placeholder='Select the job title (Optional)']"
    select_title_xpath = "//div[normalize-space()='Manager2']"
    access_xpath = "//nz-select-item[@title='Member']"
    member_xpath = "//div[contains(text(),'Member')]"
    update_btn_xpath = "//button[@type='submit']"
    delete_btn_xpath = "//tbody/tr[1]/td[5]/div[1]/nz-space[1]/div[2]/button[1]/span[1]//*[name()='svg']"
    yes_btn_xpath = "//span[normalize-space()='Yes']"
    page_selector_xpath = "//nz-select-item[@title='20 / page']"
    page_selector_10_xpath = "//nz-option-item[1]"


class SettingsTeamsLocators:
    pinTeamsTab_xpath = "//span[@class='anticon pin-button anticon-pushpin']//*[name()='svg']"


class ProjectFilesLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Testing kanban board']"
    files_xpath = "//a[normalize-space()='Files']"


class ProjectInsightsLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Testing kanban board']"
    insight_tab_xpath = "//a[normalize-space()='Insights']"
    overview_xpath = "//div[normalize-space()='Overview']"
    last_updated_tasks_xpath = "//a[normalize-space()='See all']"
    members_selector_css = "body > worklenz-root:nth-child(1) > worklenz-layout:nth-child(2) > nz-spin:nth-child(1) > div:nth-child(1) > nz-layout:nth-child(2) > nz-layout:nth-child(2) > nz-content:nth-child(1) > div:nth-child(2) > worklenz-project-view:nth-child(2) > div:nth-child(3) > div:nth-child(1) > worklenz-project-insights:nth-child(1) > nz-row:nth-child(1) > nz-segmented:nth-child(1) > div:nth-child(1) > label:nth-child(2) > div:nth-child(2)"
    # task_by_member_xpath = "css=.table-row:nth-child(2) path"
    tasks_xpath = "//div[normalize-space()='Tasks']"
    overdue_tasks_xpath = "(//a[contains(text(),'See all')])[1]"
    over_logged_tasks_xpath = "(//a[contains(text(),'See all')])[2]"
    task_completed_early_tasks_xpath = "(//a[contains(text(),'See all')])[3]"
    task_completed_late_tasks_xpath = "(//a[contains(text(),'See all')])[4]"


class ProjectMembersLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Testing kanban board']"
    members_xpath = "(//a[normalize-space()='Members'])[1]"
    refresh_btn_xpath = "//button[@nztooltiptitle='Refresh members']"
    remove_member_xpath = "(//span[@class='anticon anticon-delete'])[1]"
    ok_btn_xpath = "//span[normalize-space()='OK']"
    page_selector_xpath = "//nz-select-item[@title='20 / page']"
    pages5_select_xpath = "//nz-option-item[1]"


class ProjectRoadmapLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Testing kanban board']"
    roadmap_tab_xpath = "//a[normalize-space()='Roadmap']"


class ProjectWorkloadLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Testing kanban board']"
    create_task_btn_xpath = "//span[normalize-space()='Create Task']"
    input_task_name_xpath = "//input[@placeholder='Type your task']"
    assign_member_xpath = "(//nz-avatar[@class='ant-avatar avatar-dashed ms-1 bg-white ant-avatar-circle ant-avatar-icon ng-star-inserted'])[1]"
    select_member_xpath = "//body[1]/div[1]/div[10]/div[1]/div[1]/ul[1]/li[2]/span[1]/input[1]"
    select_workload_xpath = "//a[normalize-space()='Workload']"
    temp_click_xpath = "//label[normalize-space()='Time Estimation']"
    drawer_close_xpath = "//div[@class='ant-drawer-content-wrapper task-form-drawer-opened task-view']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']"
    workload_tab_xpath = "//a[normalize-space()='Workload']"
    member_open_xpath = "//span[@class='e-icons e-treegridcollapse']"
    open_task_xpath = "//div[@class='taskbar-custom ng-star-inserted']"
    show_start_date_xpath = "//span[normalize-space()='Show start date']"
    start_date_xpath = "//nz-date-picker[@id='task-start-date']"
    select_start_date_xpath = "//calendar-footer/div/a"
    end_date_xpath = "//input[@placeholder='End date']"
    select_end_date_xpath = "//td[@title='8/31/2023']//div[@class='ant-picker-cell-inner ng-star-inserted'][normalize-space()='31']"
    input_hours_xpath = "//input[@placeholder='Hours']"
    input_minutes_xpath = "//input[@placeholder='Minutes']"
    click_priority_xpath = "(//span[@class='me-2 ant-typography'])[1]"
    select_priority_xpath = "//nz-option-item[@title='Low']//div[@class='d-flex justify-content-between ng-star-inserted']"


class ScheduleProjectLocators:
    schedule_tab_xpath = "//strong[normalize-space()='Schedule']"
    project_dropdown_xpath = "//body[1]/worklenz-root[1]/worklenz-layout[1]/nz-spin[1]/div[1]/nz-layout[1]/nz-layout[1]/nz-content[1]/div[1]/worklenz-schedule-view[1]/div[1]/worklenz-project-schedule[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[73]/div[1]/img[1]"
    project_dropdown_close_xpath = "//img[@class='align-self-center cursor-pointer img-fluid']"
    week_selector_xpath = "//input[@placeholder='Select week']"
    week_pick_xpath = "//div[@class='ant-picker-cell-inner ng-star-inserted'][normalize-space()='25']"
    time_period_xpath = "//nz-layout[@class='ant-layout']//li[1]"
    task_click_xpath = "//h4[normalize-space()='Task1']"
    close_btn_xpath = "//span[@nztype='close']//*[name()='svg']"
    close_btn2_xpath = "//div[@class='ant-drawer-content-wrapper']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']"


class ScheduleTeamsLocators:
    schedule_tab_xpath = "//strong[normalize-space()='Schedule']"
    teams_btn_xpath = "//div[normalize-space()='Teams']"
    teams_dropdown_xpath = "//body[1]/worklenz-root[1]/worklenz-layout[1]/nz-spin[1]/div[1]/nz-layout[1]/nz-layout[1]/nz-content[1]/div[1]/worklenz-schedule-view[1]/div[1]/worklenz-team-schedule[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[145]/div[1]/img[1]"
    teams_dropdown_close_xpath = "//body[1]/worklenz-root[1]/worklenz-layout[1]/nz-spin[1]/div[1]/nz-layout[1]/nz-layout[1]/nz-content[1]/div[1]/worklenz-schedule-view[1]/div[1]/worklenz-team-schedule[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[145]/div[1]/img[1]"
    week_selector_xpath = "//input[@placeholder='Select week']"
    pick_date_xpath = "//div[@class='ant-picker-cell-inner ng-star-inserted'][normalize-space()='30']"
    time_period_xpath = "//body[1]/worklenz-root[1]/worklenz-layout[1]/nz-spin[1]/div[1]/nz-layout[1]/nz-layout[1]/nz-content[1]/div[1]/worklenz-schedule-view[1]/div[1]/worklenz-team-schedule[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[146]/ul[1]/li[4]"
    task_open_xpath = "//h4[normalize-space()='Task1']"
    task_close_xpath = "//span[@nztype='close']//*[name()='svg']"
    schedule_close_xpath = "//div[@class='ant-drawer-content-wrapper']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']"


class TaskInfoLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Testing kanban board']"
    div_taskName_xpath = "(//div[@class='flex-row task-name'])[2]"
    button_open_xpath = "(//button[@class='ant-btn plus-icon px-1 ant-btn-text'])[1]"
    assignees_css = ".ant-typography:nth-child(1) > .ant-avatar svg"
    assign_search_by_name_xpath = "//input[@placeholder='Search by name']"
    member_assign_xpath = "//li[5]/span[2]"
    temp_click_xpath = "//label[normalize-space()='When done, notify']"
    show_start_date_xpath = "//span[normalize-space()='Show start date']"
    start_date_xpath = "//input[@placeholder='Start date']"
    start_date_select_date_css = ".ant-picker-today-btn"
    end_date_xpath = "//input[@placeholder='End date']"
    end_date_select_date_xpath = "//td[@title='7/29/2023']//div[@class='ant-picker-cell-inner ng-star-inserted'][normalize-space()='29']"
    hide_start_date_xpath = "//span[normalize-space()='Hide start date']"
    time_hours_xpath = "//input[@placeholder='Hours']"
    time_minutes_xpath = "//input[@placeholder='Minutes']"
    priority_xpath = "(//nz-select-item[@title='Medium'])[2]"
    high_priority_xpath = "//span[normalize-space()='High']"
    labels_xpath = "//span/nz-tag"
    create_label_xpath = "//input[@placeholder='+ Create label']"
    done_notify_css = ".ant-typography:nth-child(1) > .ant-avatar svg"
    notify_search_by_name_xpath = "//input[@placeholder='Search by name']"
    notify_member_select_xpath = "(//li[@class='ant-checkbox-wrapper m-0 ant-checkbox-wrapper-in-form-item ant-dropdown-menu-item ng-star-inserted'])[1]"
    description_xpath = "//worklenz-task-view-description/nz-form-item/nz-form-control/div/div/div"
    enter_description_xpath = "p:nth-child(4)"
    description_paragraph_xpath = "//span[@class='tox-tbtn__select-label']"
    description_heading2_xpath = "//h2[normalize-space()='Heading 2']"
    description_numbersList_xpath = "//button[@title='Numbered list']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']"
    description_bulatList_xpath = "//button[@title='Bullet list']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']"
    description_editLink_xpath = "//button[@title='Insert/edit link']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']"
    description_Bold_xpath = "//button[@title='Bold']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']"
    description_italic_xpath = "//button[@title='Italic']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']"
    description_underline_xpath = "//button[@title='Underline']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']"
    description_Strikethrough_xpath = "//button[@title='Strikethrough']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']"
    description_editLink_URL_xpath = "//div/div/div/div/div/div/input"
    description_editLink_TextDisplay_id = "//div/div[2]/input"
    description_editLink_Title_xpath = "//div[3]/input"
    description_editLink_openLinkDw_xpath = "//span[@class='tox-listbox__select-label']"
    description_editLink_openLinkSelected_xpath = "//div[contains(text(),'Current window')]"
    description_editLink_save_xpath = "//button[@title='Save']"
    description_editLink_AlignLeft_xpath = "//button[@title='Align left']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']"
    description_editLink_AlignCenter_xpath = "//button[@title='Align center']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']"
    description_editLink_AlignRight_xpath = "//button[@title='Align right']"
    description_editLink_justify_xpath = "//button[@title='Justify']//span[@class='tox-icon tox-tbtn__icon-wrap']//*[name()='svg']"
    closeDescription_xpath = "//nz-collapse-panel[2]/div"
    clickLink_xpath = ".tox-toolbar__group:nth-child(1) > .tox-tbtn:nth-child(3) path"
    add_sub_taskBtn_xpath = "//span[normalize-space()='Add sub-task']"
    type_sub_taskInput_xpath = "//input[@placeholder='Type your task and hit enter']"
    sub_task_refreshBtn_xpath = "//span[@class='anticon anticon-reload']//*[name()='svg']"
    sub_task_priority_xpath = "//nz-tag[normalize-space()='Medium']"
    sub_task_clickChange_priority_xpath = "//worklenz-task-priority-label/div/span"
    sub_task_select_priority_xpath = "//span[normalize-space()='Low']"
    back_btn_xpath = "//button[@aria-label='Close']//div[1]"
    sub_task_status_xpath = "//nz-tag[@class='ant-tag text-dark task-list-label ant-tag-has-color']"
    sub_task_clickChange_status_xpath = "//nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-item"
    sub_task_select_status_xpath = "//div[@id='cdk-overlay-9']/nz-option-container/div/cdk-virtual-scroll-viewport/div/nz-option-item[2]/div"
    sub_task_assign_xpath = "//tbody/tr[1]/td[4]/span[1]/button[1]"
    sub_task_clickAssign_xpath = "(//nz-avatar[@class='ant-avatar avatar-dashed ms-1 bg-white ant-avatar-circle ant-avatar-icon ng-star-inserted'])[1]"
    sub_task_selectAssign_xpath = "//body[1]/div[1]/div[10]/div[1]/div[1]/ul[1]/li[3]/span[1]/input[1]"
    temp_click = "//label[normalize-space()='When done, notify']"
    sub_task_editBtn_xpath = "//button[@class='ant-btn ant-btn-sm ant-btn-icon-only ng-star-inserted']//span[@class='anticon anticon-edit']//*[name()='svg']"
    sub_task_deleteBtn_css = ".actions-row:nth-child(1) .ant-space-item:nth-child(2) svg"
    ok_btn_xpath = "//span[normalize-space()='Yes']"
    button_chooseImage_xpath = "//div[@class='ant-upload']"
    comments_input_xpath = "//textarea[@placeholder='Add a comment...']"
    comments_submit_btn_xpath = "//span[normalize-space()='Comment']"
    delete_comment_xpath = "//span[contains(text(),'Delete')]"


class TaskTimeLogLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Testing kanban board']"
    div_taskName_xpath = "(//div[@class='flex-row task-name'])[2]"
    button_open_xpath = "(//button[@class='ant-btn plus-icon px-1 ant-btn-text'])[1]"
    time_log_btn_xpath = "//div[contains(text(),'Time Log')]"
    time_play_btn_css = ".ant-btn-icon-only > .anticon-caret-right path"
    time_stop_btn_css = ".ant-btn-icon-only > .nz-icon path"
    edit_btn_xpath = "//li/button/span"
    set_hours_xpath = "//input[@placeholder='Hours']"
    set_minutes_xpath = "//input[@placeholder='Minutes']"
    set_seconds_xpath = "//input[@placeholder='Seconds']"
    date_clear_css = ".anticon-close-circle > .ng-tns-c802749266-155"
    date_picker_xpath = "//input[@placeholder='Select date']"
    select_date_xpath = "//calendar-footer/div/a"
    description_xpath = "//textarea[@id='description']"
    update_btn_xpath = "//button[@type='submit']"
    delete_btn_xpath = "//li[2]/button/span"
    delete_ok_btn_xpath = "//span[normalize-space()='OK']"
    add_time_log_btn_xpath = "//span[normalize-space()='Add Timelog']"
    export_to_excel_xpath = "//span[normalize-space()='Export to Excel']"


class TeamSelectionLocators:
    team_selection_xpath = "//span[@class='ant-dropdown-trigger rounded-pill team-name border-bottom ng-star-inserted']"
    select_team_xpath = "//span[normalize-space()='Team2']"
    team_selection2_xpath = "//span[@class='ant-dropdown-trigger rounded-pill team-name border-bottom ng-star-inserted']"
    select_team2_xpath = "//span[normalize-space()='Team N N']"


class BugsLocators:
    project_Tab_xpath = "//strong[normalize-space()='Projects']"
    project_select_xpath = "//span[normalize-space()='HomeTest']"
    project_group_By = "//span[normalize-space()='Status']"
    phase_xpath = "(//span[@class='ant-typography'][normalize-space()='Phase'])[1]"
    home_xpath = "//strong[normalize-space()='Home']"
    task_input_xpath = "(//input[@placeholder='+ Add Task'])[1]"
    select_today_xpath = "//div[@class='ant-select-item-option-content'][normalize-space()='Today']"
    select_project_xpath = "//div[contains(text(),'HomeTest')]"
    task_xpath = "//p[normalize-space()='Testing task']"
    open_task_xpath = "//span[normalize-space()='Open']"
    subTask_xpath = "//span[normalize-space()='Add sub-task']"
    enter_subtask_xpath = "//input[@placeholder='Type your task and hit enter']"


class HomeProjectLocators:
    refresh_btn_xpath = "(//button[@class='ant-btn ant-btn-circle ng-star-inserted'])[2]"
    star_xpath = "(//*[name()='path'])[49]"
    fav_tab_xpath = "//div[normalize-space()='Favorites']"
    recent_xpath = "//div[normalize-space()='Recent']"
    project_xpath = "//div[2]/span/p"


class HomeTasksLocators:
    refresh_btn_xpath = "(//button[@class='ant-btn ant-btn-circle ng-star-inserted'])[1]"
    add_task_xpath = "(//input[@placeholder='+ Add Task'])[1]"
    today_xpath = "//div[@class='ant-select-item-option-content'][normalize-space()='Today']"
    tomorrow_xpath = "//div[normalize-space()='Tomorrow']"
    next_week_xpath = "//div[normalize-space()='Next Week']"
    next_month_xpath = "//div[normalize-space()='Next Month']"
    no_due_date_xpath = "//div[contains(text(),'No Due Date')]"
    project_select_xpath = "//div[contains(text(),'HomeTest')]"
    task_xpath = "//tr[1]//td[1]//worklenz-task-name[1]//p[1]"
    task_open_xpath = "//span[normalize-space()='Open']"
    assigner_xpath = "//nz-avatar[@class='ant-avatar ant-avatar-circle ant-avatar-image ng-star-inserted']//img[@class='ng-star-inserted']"
    unSelectAssigner_xpath = "//body[1]/div[1]/div[6]/div[1]/div[1]/ul[1]/li[2]/span[2]"
    selectAssigner_xpath = "//li[2]/span[2]"
    temp_click_xpath = "//label[normalize-space()='When done, notify']"
    end_date_xpath = "//input[@placeholder='End date']"
    select_date_xpath = "//div[normalize-space()='24']"
    status_xpath = "//div/div/nz-select/nz-select-top-control/nz-select-item"
    doing_xpath = "//nz-option-item[2]/div"
    close_xpath = "//span[@nztype='close']//*[name()='svg']"
    todayTab_xpath = "//nz-tabs-nav/div/div/div[2]/div"
    upcomingTab_xpath = "//div[3]/div"
    overDueTab_xpath = "//div[4]/div"
    no_due_dateTab_xpath = "//div[5]/div"
    allTaskTab_xpath = "//nz-tabs-nav/div/div/div/div"
    dueDate_click_task_outside_xpath = "//nz-date-picker/div/input"
    dueDate_select_task_outside_xpath = "//calendar-footer/div/a"
    task_outside_click_status = "(//nz-select-item[@title='Doing'])[1]"
    task_outside_change_status = "(//nz-option-item[@title='Done'])[1]"
    click_dropDown_xpath = "//nz-select-item[@title='assigned to me']"
    select_dropDown_xpath = "//div[normalize-space()='assigned by me']"
    click_subTask_xpath = "//span[normalize-space()='Add sub-task']"
    enter_subTask_xpath = "//input[@placeholder='Type your task and hit enter']"
    calendar_tab_xpath = "//div[normalize-space()='Calendar']"
    calender_year_xpath = "//nz-select-item[@title='2023']"
    scroll_xpath = "(//cdk-virtual-scroll-viewport[@class='cdk-virtual-scroll-viewport cdk-virtual-scrollable full-width cdk-virtual-scroll-orientation-vertical'])[1]"
    calender_year_select_xpath = "//div[normalize-space()='2024']"
    calender_month_xpath = "//nz-select-item[@title='Jul']"
    calender_month_select_xpath = "//div[normalize-space()='Sep']"
    calender_date_select_xpath = "//div[contains(text(),'11')]"
    calender_year_tab_xpath = "//span[normalize-space()='Year']"
    calender_month_change_xpath = "//div[contains(text(),'Dec')]"


class HomeTodoListLocators:
    to_do_input_xpath = "//div[2]/nz-skeleton/worklenz-task-add-container/div/nz-space/div/input"
    refresh_Btn_xpath = "//button[@class='ant-btn ant-btn-circle']"
    to_do_task_done_xpath = "//tr[1]//td[1]//worklenz-task-done[1]//button[1]//span[1]//*[name()='svg']"


class WorkloadLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Test workload']"
    workload_tab_xpath = "//a[normalize-space()='Workload']"
    create_task_btn_xpath = "//span[normalize-space()='Create Task']"
    enter_task_title_xpath = "//input[@placeholder='Type your task']"
    assigner_xpath = "//span[@class='ant-typography ant-typography-secondary']//nz-avatar[@class='ant-avatar avatar-dashed ms-1 bg-white ant-avatar-circle ant-avatar-icon ng-star-inserted']"
    select_assigner_xpath = "//body[1]/div[1]/div[8]/div[1]/div[1]/ul[1]/li[2]/span[1]/input[1]"
    temporary_click_xpath = "//label[normalize-space()='When done, notify']"
    show_startDate_xpath = "//span[normalize-space()='Show start date']"
    click_startDate_xpath = "//input[@placeholder='Start date']"
    select_startDate_xpath = "//calendar-footer/div/a"
    click_endDate_xpath = "//input[@placeholder='End date']"
    select_endDate_xpath = "//td[@title='9/30/2023']//div[@class='ant-picker-cell-inner ng-star-inserted'][normalize-space()='30']"
    Set_hour_xpath = "//input[@placeholder='Hours']"
    drawer_close_btn_xpath = "//div[@class='ant-drawer-content-wrapper task-form-drawer-opened task-view']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']"
    Expand_all_xpath = "//span[normalize-space()='Expand all']"
    Assigned_task_open_xpath = "//div[@class='taskbar-custom ng-star-inserted']"
    click_subTask_xpath = "//span[normalize-space()='Add sub-task']"
    enter_subTask_xpath = "//input[@placeholder='Type your task and hit enter']"
    subtask_open_xpath = "//td[normalize-space()='Workload subTask']"
    select_subTask_assigner_xpath = "//body[1]/div[1]/div[8]/div[1]/div[1]/ul[1]/li[3]/span[2]"
    back_btn_subTask_xpath = "//button[@aria-label='Close']//div[1]"


class RoadmapLocators:
    project_tab_xpath = "//strong[normalize-space()='Projects']"
    select_project_xpath = "//span[normalize-space()='Test roadmap']"
    Roadmap_tab_xpath = "//a[normalize-space()='Roadmap']"
    Add_task_btn_xpath = "//span[normalize-space()='Add Task']"
    Task_title_input_xpath = "//input[@placeholder='Type your task']"
    assigner_xpath = "//span[@class='ant-typography ant-typography-secondary']//nz-avatar[@class='ant-avatar avatar-dashed ms-1 bg-white ant-avatar-circle ant-avatar-icon ng-star-inserted']"
    select_assigner_xpath = "//body[1]/div[1]/div[8]/div[1]/div[1]/ul[1]/li[2]/span[1]/input[1]"
    temporary_click_xpath = "//label[normalize-space()='When done, notify']"
    show_startDate_xpath = "//span[normalize-space()='Show start date']"
    click_startDate_xpath = "//input[@placeholder='Start date']"
    select_startDate_xpath = "//calendar-footer/div/a"
    click_endDate_xpath = "//input[@placeholder='End date']"
    select_endDate_xpath = "//td[@title='10/30/2023']//div[@class='ant-picker-cell-inner ng-star-inserted'][normalize-space()='30']"
    select_endDate_subTask_xpath = "//td[@title='10/18/2023']//div[@class='ant-picker-cell-inner ng-star-inserted'][normalize-space()='18']"
    Set_hour_xpath = "//input[@placeholder='Hours']"
    click_subTask_xpath = "//span[normalize-space()='Add sub-task']"
    enter_subTask_xpath = "//input[@placeholder='Type your task and hit enter']"
    subtask_open_xpath = "//td[contains(text(),'Roadmap sub Task')]"
    drawer_close_btn_xpath = "//div[@class='ant-drawer-content-wrapper task-form-drawer-opened task-view']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']"
    back_btn_xpath = "//button[@aria-label='Close']//div[1]"
    parentTaskRightClick_xpath = "//td[@aria-label='Roadmap Task column header Task Name']//div[@class='e-treecolumn-container']"
    parentTaskRightClick_addSubTask_xpath = "//li[@id='add-subtask']"
    expand_all_xpath = "//span[normalize-space()='Expand all']"
    collapse_all_xpath = "//span[normalize-space()='Collapse all']"
    zoom_in_xpath = "//span[normalize-space()='Zoom in']"
    zoom_out_xpath = "//span[normalize-space()='Zoom out']"
    zoom_in_fit_xpath = "//span[normalize-space()='Zoom to fit']"
    show_phases_xpath = "//span[normalize-space()='Show Phase']"


class ReportingMembersLocators:
    reporting_tab_xpath = "//strong[normalize-space()='Reporting']"
    members_tab_xpath = "//li[@class='ant-menu-item'][normalize-space()='Members']"
    include_archived_project_xpath = "//span[normalize-space()='Include Archived Projects']"
    time_range_last_week_btn_xpath = "//span[normalize-space()='Last week']"
    time_range_yesterday_btn_xpath = "//span[normalize-space()='Yesterday']"
    time_range_lastMonth_btn_xpath = "//span[normalize-space()='Last month']"
    time_range_quarter_btn_xpath = "//li[normalize-space()='Last quarter']"
    time_range_yesterday_xpath = "//li[normalize-space()='Yesterday']"
    time_range_lastWeek_xpath = "//li[normalize-space()='Last week']"
    time_range_lastMonth_xpath = "//li[normalize-space()='Last month']"
    time_range_lastQuarter_xpath = "//li[normalize-space()='Last quarter']"
    time_range_startDate_xpath = "//input[@placeholder='Start date']"
    time_range_selectStartDate_xpath = "//td[@title='10/2/2023']//div[@class='ant-picker-cell-inner ng-star-inserted'][normalize-space()='2']"
    time_range_endDate_xpath = "//input[@placeholder='End date']"
    time_range_selectEndDate_xpath = "//td[@title='11/30/2023']//div[@class='ant-picker-cell-inner ng-star-inserted'][normalize-space()='30']"
    filter_btn_xpath = "//span[normalize-space()='Filter']"
    export_btn_xpath = "//nz-page-header-extra[@class='ant-page-header-heading-extra']//button[@class='ant-btn ant-dropdown-trigger ant-btn-primary ng-star-inserted']"
    export_to_excel_xpath = "//li[@class='ant-dropdown-menu-item ng-star-inserted']"

