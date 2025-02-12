
CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    start_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    position TEXT
);

CREATE TABLE task (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    due_date DATE,
    project_id INTEGER NOT NULL REFERENCES project(id) ON DELETE CASCADE
);

CREATE TABLE assignment (
    id SERIAL PRIMARY KEY,
    task_id INTEGER NOT NULL REFERENCES task(id) ON DELETE CASCADE,
    employee_id INTEGER NOT NULL REFERENCES employee(id) ON DELETE CASCADE
);


INSERT INTO "public"."project" ("id", "name", "description", "start_date") VALUES ('1', 'PwC Challenge', 'Create in 7 days a layered FastAPI REST API.', '2025-01-29 19:22:21.189137+00'), ('12', 'Mobile App Development', 'Development of a mobile app for task management.', '2025-02-01 09:00:00+00'), ('13', 'E-learning Platform', 'Creation of an online learning platform.', '2025-10-05 10:00:00+00'), ('14', 'Inventory Management System', 'Development of a real-time inventory management system.', '2025-03-10 11:00:00+00'), ('15', 'Digital Marketing Campaign', 'Digital marketing campaign for a new product launch.', '2025-04-15 12:00:00+00'), ('16', 'Sales Process Automation', 'Automation of sales processes using AI.', '2025-05-20 13:00:00+00');


INSERT INTO "public"."employee" ("id", "name", "email", "position") VALUES ('1', 'John Doe', 'jodo@mycompany.com', 'Administrative assistant'), ('2', 'Tim Anderson', 'tian@company.com', 'Software developer'), ('3', 'Mary Timmons', 'mati@company.com', 'Sales manager'), ('6', 'Juan Pérez', 'juan.perez@example.com', 'Senior Developer'), ('7', 'María Gómez', 'maria.gomez@example.com', 'Frontend Developer'), ('8', 'Carlos López', 'carlos.lopez@example.com', 'Backend Developer'), ('9', 'Ana Martínez', 'ana.martinez@example.com', 'UX/UI Designer'), ('10', 'Luis Rodríguez', 'luis.rodriguez@example.com', 'DevOps Engineer'), ('11', 'Sofía Hernández', 'sofia.hernandez@example.com', 'Data Analyst'), ('12', 'Pedro Díaz', 'pedro.diaz@example.com', 'Project Manager'), ('13', 'Laura Ruiz', 'laura.ruiz@example.com', 'Digital Marketing Specialist'), ('14', 'Jorge Sánchez', 'jorge.sanchez@example.com', 'SEO Specialist'), ('15', 'Mónica Álvarez', 'monica.alvarez@example.com', 'Social Media Specialist'), ('16', 'Ricardo Torres', 'ricardo.torres@example.com', 'Sales Executive'), ('17', 'Elena Castro', 'elena.castro@example.com', 'Marketing Coordinator'), ('18', 'Diego Morales', 'diego.morales@example.com', 'Market Analyst'), ('19', 'Carmen Ortega', 'carmen.ortega@example.com', 'Sales Assistant'), ('20', 'Fernando Jiménez', 'fernando.jimenez@example.com', 'Business Consultant');


INSERT INTO "public"."task" ("id", "name", "due_date", "project_id") VALUES ('1', 'Review documentation for async with SQLModel.', '2025-01-31', '1'), ('2', 'Create testing for all endpoints', '2025-01-29', '1'), ('3', 'Implement UUID middleware', '2025-01-29', '1'), ('6', 'Design Course Structure', '2023-11-15', '13'), ('7', 'Develop User Authentication', '2023-11-20', '13'), ('8', 'Create Course Content', '2023-11-25', '13'), ('9', 'Implement Payment Gateway', '2023-11-30', '13'), ('10', 'Test Platform Functionality', '2023-12-05', '13'), ('11', 'Optimize Platform Performance', '2023-12-10', '13'), ('12', 'Deploy Platform to Production', '2023-12-15', '13'), ('13', 'Monitor Platform Usage', '2023-12-20', '13'), ('14', 'Update Course Content', '2023-12-25', '13'), ('15', 'Fix Bugs in Platform', '2023-12-30', '13'), ('16', 'Design App UI/UX', '2023-11-15', '12'), ('17', 'Develop App Backend', '2023-11-20', '12'), ('18', 'Implement Push Notifications', '2023-11-25', '12'), ('19', 'Integrate API for Data Sync', '2023-11-30', '12'), ('20', 'Test App on Multiple Devices', '2023-12-05', '12'), ('21', 'Optimize App Performance', '2023-12-10', '12'), ('22', 'Deploy App to App Stores', '2023-12-15', '12'), ('23', 'Monitor App Crashes', '2023-12-20', '12'), ('24', 'Update App Features', '2023-12-25', '12'), ('25', 'Fix Bugs in App', '2023-12-30', '12'), ('26', 'Create Marketing Strategy', '2023-11-15', '15'), ('27', 'Design Social Media Ads', '2023-11-20', '15'), ('28', 'Launch Email Campaign', '2023-11-25', '15'), ('29', 'Analyze Campaign Performance', '2023-11-30', '15'), ('30', 'Optimize Ad Spend', '2023-12-05', '15'), ('31', 'Engage with Social Media Followers', '2023-12-10', '15'), ('32', 'Monitor Campaign ROI', '2023-12-15', '15'), ('33', 'Update Marketing Content', '2023-12-20', '15'), ('34', 'Run A/B Tests', '2023-12-25', '15'), ('35', 'Generate Campaign Report', '2023-12-30', '15'), ('36', 'Design Database Schema', '2023-11-15', '14'), ('37', 'Develop Inventory Tracking Module', '2023-11-20', '14'), ('38', 'Implement Barcode Scanning', '2023-11-25', '14'), ('39', 'Integrate with Supplier APIs', '2023-11-30', '14'), ('40', 'Test System Accuracy', '2023-12-05', '14'), ('41', 'Optimize System Performance', '2023-12-10', '14'), ('42', 'Deploy System to Production', '2023-12-15', '14'), ('43', 'Monitor System Alerts', '2023-12-20', '14'), ('44', 'Update Inventory Data', '2023-12-25', '14'), ('45', 'Fix Bugs in System', '2023-12-30', '14'), ('46', 'Research Industry Trends', '2023-11-15', '1'), ('47', 'Develop Business Case', '2023-11-20', '1'), ('48', 'Create Presentation Slides', '2023-11-25', '1'), ('49', 'Prepare Financial Models', '2023-11-30', '1'), ('50', 'Test Solution Feasibility', '2023-12-05', '1'), ('51', 'Optimize Solution Design', '2023-12-10', '1'), ('52', 'Present Solution to Stakeholders', '2023-12-15', '1'), ('53', 'Monitor Feedback', '2023-12-20', '1'), ('54', 'Update Solution Proposal', '2023-12-25', '1'), ('55', 'Finalize Deliverables', '2023-12-30', '1'), ('56', 'Analyze Sales Processes', '2023-11-15', '16'), ('57', 'Design Automation Workflow', '2023-11-20', '16'), ('58', 'Develop Automation Scripts', '2023-11-25', '16'), ('59', 'Integrate with CRM System', '2023-11-30', '16'), ('60', 'Test Automation Accuracy', '2023-12-05', '16'), ('61', 'Optimize Automation Performance', '2023-12-10', '16'), ('62', 'Deploy Automation to Production', '2023-12-15', '16'), ('63', 'Monitor Automation Results', '2023-12-20', '16'), ('64', 'Update Automation Rules', '2023-12-25', '16'), ('65', 'Fix Bugs in Automation', '2023-12-30', '16');


INSERT INTO "public"."assignment" ("id", "task_id", "employee_id") VALUES ('1', '1', '2'), ('2', '2', '3'), ('3', '3', '2'), ('253', '6', '3'), ('254', '7', '3'), ('255', '8', '2'), ('256', '9', '2'), ('257', '10', '6'), ('258', '11', '6'), ('259', '12', '6'), ('260', '16', '7'), ('261', '17', '7'), ('262', '18', '7'), ('263', '19', '8'), ('264', '20', '8'), ('265', '21', '8'), ('266', '22', '9'), ('267', '23', '9'), ('268', '24', '9'), ('269', '25', '10'), ('270', '36', '10'), ('271', '37', '10'), ('272', '38', '11'), ('273', '39', '11'), ('274', '40', '11'), ('275', '41', '12'), ('276', '42', '12'), ('277', '43', '12'), ('278', '26', '1'), ('279', '27', '1'), ('280', '28', '1'), ('281', '29', '6'), ('282', '30', '6'), ('283', '31', '6'), ('284', '32', '6'), ('285', '33', '6'), ('286', '34', '6'), ('287', '56', '7'), ('288', '57', '7'), ('289', '58', '7'), ('290', '59', '8'), ('291', '60', '8'), ('292', '61', '8'), ('293', '62', '9'), ('294', '63', '9'), ('295', '64', '9'), ('296', '65', '10'), ('297', '46', '10'), ('298', '47', '10'), ('299', '48', '11'), ('300', '49', '11'), ('301', '50', '11'), ('302', '51', '1'), ('303', '52', '1'), ('304', '53', '1');


