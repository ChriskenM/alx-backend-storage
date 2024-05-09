-- Creates first name index
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
