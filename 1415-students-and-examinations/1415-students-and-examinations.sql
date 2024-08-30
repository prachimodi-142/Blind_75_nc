# Write your MySQL query statement below
select st.student_id, st.student_name, sub.subject_name, 
    COUNT(e.subject_name) AS attended_exams 
from Students st 
join Subjects sub
left join Examinations e on sub.subject_name = e.subject_name
and e.student_id = st.student_id
group by sub.subject_name, st.student_id
order by st.student_id, sub.subject_name;
