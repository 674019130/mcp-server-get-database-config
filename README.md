# mcp-server-get-database-config

Create a new file named `database.json` based on the structure shown in the given sample file `database-example.json`, and fill in the database-related information.

**With the following prompt, the MCP Client can automatically retrieve the database configuration**, eliminating the need to manually provide it when generating simple analysis scripts, thereby improving Talk efficiency.

```
帮我写个python脚本，
在 db_alpha 库执行
select ex.device_id as id, ex.group_no
from service_config_alpha ex
where ex.is_active = 1
  and ex.status = 1
union all
select dv.id, dv.group_no
from device_config_beta dv
where dv.is_active = 1
  and dv.status = 1

语句，得到所有的服务端设备ID、所属组号（group_no）。

拿到这些 server，在 db_beta 库执行
select loc.region,
       count(1),
from connection_log cnt
         left join device_location loc on loc.id = cnt.client_id
where server_id in (
    # 这里填入单台 server 
)
group by loc.region

得到单台 server 的区域分布。但是拿到的结果中，有可能存在 region 为空的情况，这些是因为 connection_log 表中 client_id 并不在 db_beta 的 device_location 表中。

所以需要将这些 client_id 再拿到 db_alpha 库的 device_location 表中查询，将结果合并。
select loc.region,
       count(1)
       from device_location loc
       where loc.id in (
        # 这里填入单台 server 的区域分布结果中为空的 client_id
       )
       group by loc.region

最后，将两部分结果合并，得到单台 server 的区域分布。
计算区域分布的百分比，计算变异系数，使用 pyecharts 画单台 server 的区域分布百分比图。

再计算每个组的区域分布百分比，计算变异系数，使用 pyecharts 画每个组的区域分布百分比图。

再计算每个组的平均变异系数，使用 pyecharts 画每个组的平均变异系数柱状图。

```
