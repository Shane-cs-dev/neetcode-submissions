-- Write your query below

-- SELECT DISTINCT ON (student_id)
--     student_id,
--     exam_id,
--     score
-- FROM exam_results
-- ORDER BY student_id, score DESC, exam_id;


-- Common table expression (CTE)
-- Windown function

with ranked_data as (
    select student_id, 
    exam_id, 
    score,
    row_number() over (partition by student_id order by score desc, exam_id asc)
    as rn
    from exam_results
)

select student_id, exam_id, score from ranked_data
    where rn = 1
    order by student_id;