INSERT INTO BANK (ID_BANK, NM_BANK) VALUES ('237', 'BRADESCO');
INSERT INTO PAYER (ID_PAYER, UUID_CUSTOMER, NM_PAYER, NU_ENTRY, TP_ENTRY, NU_POSTAL_CODE, DS_STREET, DS_NUMBER, NM_NEIGHBORHOOD, NM_CITY, NM_STATE) VALUES (1, '12345678901234567890', 'NEXXERA', '12312123', '1', '88010002', 'Felipe Schmidt', '123', 'Centro', 'Fpolis', 'SC');
INSERT INTO PAYER (ID_PAYER, UUID_CUSTOMER, NM_PAYER, NU_ENTRY, TP_ENTRY, NU_POSTAL_CODE, DS_STREET, DS_NUMBER, NM_NEIGHBORHOOD, NM_CITY, NM_STATE) VALUES (2, '00011122233344455666', 'NEXXERA', '123123', '2', '88010000', 'Rua Felipe Schmidt', '22', 'Centro', 'Fpolis', 'SC');
INSERT INTO BANKING_AGREEMENT (ID_AGREEMENT, ID_PAYER, ID_BANK_SETUP, NU_AGREEMENT, NU_BRANCH, DV_BRANCH, NU_ACCOUNT, DV_ACCOUNT, DV_BRANCH_ACCOUNT) VALUES (1, 1, '1', '1', 1, '1', 1, '1', 1);
INSERT INTO BANKING_ENTRY (ID_BANKING_ENTRY, NM_BANKING_ENTRY) VALUES (1, 'TED')
