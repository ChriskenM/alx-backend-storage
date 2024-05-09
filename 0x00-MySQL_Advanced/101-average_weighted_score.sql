-- Create the ComputeAverageWeightedScoreForUsers stored procedure
DELIMITER //;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_user_id INT;
    DECLARE v_total_score FLOAT;
    DECLARE v_total_weight INT;
    DECLARE cur_users CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open cursor for users
    OPEN cur_users;

    -- Loop through users
    user_loop: LOOP
        FETCH cur_users INTO v_user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Initialize variables
        SET v_total_score = 0;
        SET v_total_weight = 0;

        -- Calculate total weighted score for the user
        SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
        INTO v_total_score, v_total_weight
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = v_user_id;

        -- Compute average weighted score
        IF v_total_weight > 0 THEN
            UPDATE users
            SET average_score = v_total_score / v_total_weight
            WHERE id = v_user_id;
        ELSE
            UPDATE users
            SET average_score = 0
            WHERE id = v_user_id;
        END IF;
    END LOOP;

    -- Close cursor
    CLOSE cur_users;
    
END; //

DELIMITER ;

