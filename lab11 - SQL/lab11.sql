.read sp20data.sql

CREATE TABLE obedience AS
  SELECT seven as obedience, instructor from students;

CREATE TABLE smallest_int AS
  SELECT time, smallest from students
  WHERE smallest > 2 ORDER BY smallest LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color
  FROM students as a, students as b
  WHERE a.pet = b.pet AND a.song = b.song 
  AND a.time < b.time;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here


CREATE TABLE stacks AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
