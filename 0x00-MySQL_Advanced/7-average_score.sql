-- Create stored procedure ComputeAverageScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE v_total_score FLOAT;
    DECLARE v_total_projects INT;
    
    -- Compute total score and total number of projects for the user
    SELECT SUM(score), COUNT(*) INTO v_total_score, v_total_projects
    FROM corrections
    WHERE user_id = p_user_id;
    
    -- Calculate average score and update user's average_score attribute
    IF v_total_projects > 0 THEN
        UPDATE users
        SET average_score = v_total_score / v_total_projects
        WHERE id = p_user_id;
    END IF;
END //

DELIMITER ;

