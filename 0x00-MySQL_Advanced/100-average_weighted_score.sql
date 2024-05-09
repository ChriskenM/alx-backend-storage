-- Create the ComputeAverageWeightedScoreForUser stored procedure
DELIMITER //;`

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE v_total_score FLOAT;
    DECLARE v_total_weight INT;
    
    -- Initialize variables
    SET v_total_score = 0;
    SET v_total_weight = 0;

    -- Calculate total weighted score
    SELECT SUM(score * weight) INTO v_total_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = p_user_id;

    -- Calculate total weight
    SELECT SUM(weight) INTO v_total_weight
    FROM projects;

    -- Compute average weighted score
    IF v_total_weight > 0 THEN
        UPDATE users
        SET average_score = v_total_score / v_total_weight
        WHERE id = p_user_id;
    ELSE
        UPDATE users
        SET average_score = 0
        WHERE id = p_user_id;
    END IF;
    
END; //

DELIMITER ;

