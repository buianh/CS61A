CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-- copy your solution from prev hw!
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT 'abraham' AS name, 'toy' as size UNION
  SELECT "barack"         , 'standard'           UNION
  SELECT "clinton"        , 'standard'         UNION
  SELECT "delano"         , 'standard'         UNION
  SELECT "eisenhower"     , 'mini'          UNION
  SELECT "fillmore"       , 'mini'           UNION
  SELECT "grover"         , 'toy'           UNION
  SELECT "herbert"        , 'mini';

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child 
  FROM parents as a, dogs as b
  WHERE a.parent = b.name ORDER BY b.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child as sib1, b.child as sib2, c.size as sib1_size
  FROM parents as a, parents as b, size_of_dogs as c
  WHERE a.parent = b.parent and a.child < b.child and a.child = c.name;
  
CREATE TABLE siblings2 AS
  SELECT a.sib1, a.sib2, b.size
  FROM siblings as a, size_of_dogs as b
  WHERE a.sib2 = b.name AND a.sib1_size = b.size;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.sib1 || ' and ' || a.sib2 ||' are ' || a.size || ' siblings'
  FROM siblings2 as a;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper SELECT name, height, height FROM dogs;
INSERT INTO stacks_helper SELECT a.dogs || ', ' || b.name, a.stack_height+b.height, b.height
			FROM stacks_helper as a, dogs as b
			WHERE a.last_height < b.height;
INSERT INTO stacks_helper SELECT a.dogs || ', ' || b.name, a.stack_height+b.height, b.height
			FROM stacks_helper as a, dogs as b
			WHERE a.last_height < b.height;
INSERT INTO stacks_helper SELECT a.dogs || ', ' || b.name, a.stack_height+b.height, b.height
			FROM stacks_helper as a, dogs as b
			WHERE a.last_height < b.height;

CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper
  WHERE stack_height > 170
  ORDER BY stack_height;
