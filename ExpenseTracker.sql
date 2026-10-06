CREATE TABLE `users` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `username` varchar(50) UNIQUE NOT NULL,
  `email` varchar(255) UNIQUE NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL
);

CREATE TABLE `financial_profiles` (
  `user_id` integer PRIMARY KEY,
  `opening_balance` decimal(12,2) NOT NULL DEFAULT 0,
  `balance_start_date` date NOT NULL,
  `savings_opening_balance` decimal(12,2) NOT NULL DEFAULT 0,
  `savings_start_date` date NOT NULL,
  `updated_at` timestamp
);

CREATE TABLE `incomes` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `name` varchar(100) NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `frequency` varchar(20) NOT NULL,
  `next_expected_date` date NOT NULL,
  `is_active` boolean NOT NULL DEFAULT true,
  `updated_at` timestamp
);

CREATE TABLE `income_entries` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `income_id` integer,
  `amount` decimal(12,2) NOT NULL,
  `expected_date` date NOT NULL,
  `received_date` date,
  `status` varchar(20) NOT NULL DEFAULT 'pending',
  `description` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `debts` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `name` varchar(100) NOT NULL,
  `debt_type` varchar(50) NOT NULL,
  `opening_balance` decimal(12,2) NOT NULL,
  `balance_start_date` date NOT NULL,
  `annual_interest_rate` decimal(7,4) NOT NULL,
  `interest_method` varchar(30) NOT NULL,
  `minimum_payment` decimal(12,2),
  `payment_due_day` integer,
  `statement_day` integer,
  `updated_at` timestamp
);

CREATE TABLE `debt_payments` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `debt_id` integer NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `principal_paid` decimal(12,2) NOT NULL,
  `interest_paid` decimal(12,2) NOT NULL,
  `payment_date` date NOT NULL,
  `created_at` timestamp
);

CREATE TABLE `planned_debt_payments` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `debt_id` integer NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `planned_date` date NOT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'planned',
  `actual_payment_id` integer UNIQUE
);

CREATE TABLE `debt_adjustments` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `debt_id` integer NOT NULL,
  `adjustment_type` varchar(30) NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `effective_date` date NOT NULL,
  `description` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `savings_goals` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `name` varchar(100) NOT NULL,
  `target_amount` decimal(12,2) NOT NULL,
  `current_amount` decimal(12,2) NOT NULL DEFAULT 0,
  `created_at` timestamp,
  `updated_at` timestamp
);

CREATE TABLE `savings_transactions` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `transaction_type` varchar(30) NOT NULL,
  `affects_available_cash` boolean NOT NULL DEFAULT false,
  `transaction_date` date NOT NULL,
  `description` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `categories` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer,
  `name` varchar(100) NOT NULL,
  `created_at` timestamp
);

CREATE TABLE `expenses` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `category_id` integer NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `description` varchar(255),
  `expense_date` date NOT NULL,
  `created_at` timestamp,
  `payment_method` varchar(20) NOT NULL DEFAULT 'cash',
  `debt_id` integer,
  `recurring_rule_id` integer,
  `recurring_due_date` date
);

CREATE TABLE `recurring_expenses` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer NOT NULL,
  `category_id` integer NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `description` varchar(255),
  `payment_method` varchar(20) NOT NULL DEFAULT 'cash',
  `debt_id` integer,
  `frequency` varchar(20) NOT NULL,
  `start_date` date NOT NULL,
  `next_due_date` date NOT NULL,
  `end_date` date,
  `is_active` boolean NOT NULL DEFAULT true
);

CREATE TABLE `recurring_expense_exceptions` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `recurring_rule_id` integer NOT NULL,
  `occurrence_date` date NOT NULL,
  `reason` varchar(50) NOT NULL DEFAULT 'skipped'
);

CREATE UNIQUE INDEX `income_entries_index_0` ON `income_entries` (`income_id`, `expected_date`);

CREATE UNIQUE INDEX `expenses_index_1` ON `expenses` (`recurring_rule_id`, `recurring_due_date`);

CREATE UNIQUE INDEX `recurring_expense_exceptions_index_2` ON `recurring_expense_exceptions` (`recurring_rule_id`, `occurrence_date`);

ALTER TABLE `financial_profiles` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `incomes` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `income_entries` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `income_entries` ADD FOREIGN KEY (`income_id`) REFERENCES `incomes` (`id`);

ALTER TABLE `debts` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `debt_payments` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `debt_payments` ADD FOREIGN KEY (`debt_id`) REFERENCES `debts` (`id`);

ALTER TABLE `planned_debt_payments` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `planned_debt_payments` ADD FOREIGN KEY (`debt_id`) REFERENCES `debts` (`id`);

ALTER TABLE `planned_debt_payments` ADD FOREIGN KEY (`actual_payment_id`) REFERENCES `debt_payments` (`id`);

ALTER TABLE `debt_adjustments` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `debt_adjustments` ADD FOREIGN KEY (`debt_id`) REFERENCES `debts` (`id`);

ALTER TABLE `savings_goals` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `savings_transactions` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `categories` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `expenses` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `expenses` ADD FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);

ALTER TABLE `expenses` ADD FOREIGN KEY (`debt_id`) REFERENCES `debts` (`id`);

ALTER TABLE `recurring_expenses` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `recurring_expenses` ADD FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);

ALTER TABLE `recurring_expenses` ADD FOREIGN KEY (`debt_id`) REFERENCES `debts` (`id`);

ALTER TABLE `expenses` ADD FOREIGN KEY (`recurring_rule_id`) REFERENCES `recurring_expenses` (`id`);

ALTER TABLE `recurring_expense_exceptions` ADD FOREIGN KEY (`recurring_rule_id`) REFERENCES `recurring_expenses` (`id`);
