# 官方资料起点与待核条件（CN / US / UK）

> 根据赵敏2026-10-21的6张官方种子卡摘录。**只用于识别应核实哪些因素和定位来源；不是2026年逐一完成复核的个人法律结论。** 调用前核管辖地、资格、现行条文及页面更新时间；不得假称已联网验证。

核查时间：2026-10-21（北京时间）；研究Owner：赵敏。**仅用于构建问题树和首轮测试，不是可直接销售的法律知识包。** 所有条目只按官网当前可见内容记录，受规则更新、法域、劳动关系类型和个人事实影响，不推定用户符合资格。

## CN-EMP-001 中国劳动合同解除/经济补偿
- 官方源：中华人民共和国人力资源和社会保障部《中华人民共和国劳动合同法》 https://www.mohrss.gov.cn/xxgk2020/fdzdgknr/zcfg/fl/202011/t20201102_394622_wap.html
- 事实：该法第46条列出用人单位应支付经济补偿的情形，不能把“任何员工主动辞职”一概等同依法可以拿经济补偿；第38条条件与具体解除原因需核。
- 关键变量：雇主违法/双方协商/劳动者单方原因、劳动合同、入职年限、所在地、解除证明、争议证据。
- 适用：中华人民共和国大陆劳动法律关系；假定是劳动关系时，不能套到独立承包或特殊用工未经核实情形。
- 资料状态：官方原文已检索；个人适用性未审/未核最新司法解释，`VERIFIED_SOURCE / APPLICATION_PENDING`。

## CN-UI-002 中国失业保险领取条件
- 官方源：国务院政府网《失业保险条例》 https://www.gov.cn/banshi/2005-08/04/content_20258.htm
- 事实：官网列有参保缴费、非因本人意愿中断就业、失业登记及求职要求等条件；**本条为早期法规网页**，必须再查国务院及当地现行配套条款、资格变化和经办要求，不能直接给2026年领取结论。
- 关键变量：参保所在城市、缴费时间、失业原因、现行地方经办规则。
- 状态：`HISTORICAL_OFFICIAL_SOURCE / CURRENT_RULE_RECHECK_REQUIRED`。

## US-CA-UI-001 美国加州失业金：辞职≠自动可领
- 官方源：California Employment Development Department (EDD), Unemployment Insurance Eligibility https://edd.ca.gov/UI_Eligibility 及 FAQ https://edd.ca.gov/en/unemployment/faq_-_eligibility
- 事实：加州福利有就业/收入/可用可工作/求职等资格；主动辞职或被解雇需要EDA个案原因调查；主动离职须证实有正当原因及合理保留工作努力，不能凭用户说“辞职”就计算将来领取金额。
- 变量：雇员身份、历史工资、实际退出原因、移民工作授权、求职状态、州内批准结果。
- 状态：`VERIFIED_SOURCE / INDIVIDUAL_ENTITLEMENT_UNDETERMINED`。

## US-FMLA-002 美国联邦FMLA休假不能等同带薪收入
- 官方源：U.S. Department of Labor Fact Sheet #28（March 2025 revision）https://www.dol.gov/agencies/whd/fact-sheets/28-fmla
- 事实：合格员工有工作保护及团体健康福利维持，但FMLA假期本身可不带薪，另需看公司/州福利；适用要求涵盖雇主、工龄、工时与所在地人员数。
- 状态：`VERIFIED_SOURCE / STATE_EMPLOYER_RECHECK_REQUIRED`。

## UK-RED-001 英国裁员法定补偿前提
- 官方源：GOV.UK Redundancy Rights https://www.gov.uk/redundancy-your-rights/redundancy-pay
- 事实：一般需雇员身份且对该雇主工作满2年才可能有法定裁员补偿；计算受工龄、年龄、法定封顶及情况影响。不能对所有英国居住者统一假定有补偿。
- 状态：`VERIFIED_SOURCE / CHECK_UK_NATION_AND_EXCEPTIONS`。

## UK-CONSULT-002 英国裁员磋商程序
- 官方源：GOV.UK https://www.gov.uk/redundancy-your-rights/consultation
- 事实：裁员有磋商要求，较大规模裁员还涉及集体磋商；英国不同法域和劳动关系差别仍需核，不能给不符合条件用户承诺必得赔偿。
- 状态：`VERIFIED_SOURCE / CHECK_LIVE_RULES_BEFORE_PRODUCT`。

## 知识库使用规则
任何上述卡片只能用于构建“问题→要核查资格→可能的决策路径”，不可直接成为普适法律结论；有矛盾则以官方最新有效文本为准。本初稿为赵敏本人联网原文来源核验，不涉及Spark/Flash检索，没有虚构用户具体权益。


## 已声明但尚不能作为商品内数据的其他研究
双儿交接报告提及五国70张官方卡、40问和22案例审计JSON，但本次可读取的18-muse资料中仅有**代表性文字摘要**，未取得被报告点名的`wdi_sources_registry_v2.jsonl`、`wdi_40_questions_v2.json`、`wdi_22_cases_audit_v2.json`原始结构化文件。不能把这些计数或自测“零错”宣传成仓库已经含有70张逐条可调用、已独立复核的官方事实卡。
