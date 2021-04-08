### index usage
- always run ANALYZE first
- EXPLAIN command 

### index-only scan
- visbility map is on the table's heap (main data area)
- covering index
  - create index tab_x_y on tab(x) include (y);
  - to help queries: select y from tab where x = 'key';
