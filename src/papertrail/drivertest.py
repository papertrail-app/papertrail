from papertraildriver import PaperTrailDriver


driver = PaperTrailDriver()

driver.encrypt('password', './testimg.png', './papertrail_drivertest.pdf')
driver.decrypt('password', './papertrail_drivertest.pdf', 'imgtest_out.png')
