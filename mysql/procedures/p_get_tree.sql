DELIMITER $$

DROP PROCEDURE IF EXISTS `p_get_tree`$$

CREATE PROCEDURE `p_get_tree`(
    node_id INT UNSIGNED
) COMMENT 'Query all descendants nodes by a node id, return as a result set'
BEGIN
  SELECT
    node.`id`,
    node.`is_deleted`,
    node.`parent_id`,
    node.`account_id`,
    node.`branch_id`,
	node.`type`,
    CONCAT(
        REPEAT('-', path.`path_length`),
        node.`name`
    ) AS name,
    path.`path_length`,
    GROUP_CONCAT(
        crumbs.`ancestor_id` SEPARATOR ','
    ) AS breadcrumbs,
    node.`account_id`,
    node.`branch_id`,
    node.`type`
  FROM
    `prefix_nodes` AS node
    JOIN `prefix_nodes_paths` AS path
      ON node.`id` = path.`descendant_id`
    JOIN `prefix_nodes_paths` AS crumbs
      ON crumbs.`descendant_id` = path.`descendant_id`
  WHERE path.`ancestor_id` = `node_id`
    AND node.`is_deleted` = 0
  GROUP BY node.`id`
  ORDER BY breadcrumbs ;
END$$

DELIMITER ;
