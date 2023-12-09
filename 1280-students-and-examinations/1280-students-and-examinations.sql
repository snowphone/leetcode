with key_table as (
    select s.student_id, s.student_name, Subjects.subject_name
    from Students s
    cross join Subjects
)
select k.student_id, k.student_name, k.subject_name, count(e.subject_name) as attended_exams
from key_table as k
left join Examinations e on k.student_id = e.student_id and k.subject_name = e.subject_name
group by k.student_id, k.student_name, k.subject_name
order by k.student_id, k.subject_name
