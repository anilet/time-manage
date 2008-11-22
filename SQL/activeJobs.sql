drop view `management`.`activeJobs` ;

CREATE
    /*[ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = { user | CURRENT_USER }]
    [SQL SECURITY { DEFINER | INVOKER }]*/
    VIEW `management`.`activeJobs` 
    AS
    (SELECT * FROM `jobs1` WHERE `isActive` = '1' OR FK_jobstatus_Id = 0)

