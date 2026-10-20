# 地区化产品与素材库协议 / 2026-10-20
本文件不是现行法律速查表。任何法规数字、资格、时限都必须由负责研究的 Agent 核查官方来源并填写来源与查询日期；没有来源时只输出待核问题。

## 产品线结构
Core Engine（共用） + Locale Pack（国家/地区） + Scenario Pack（人生议题） + Risk Gate（统一安全） + Case Evidence（可审计来源）。
语言不等于辖区：中文用户可能居住美国/加拿大，英语用户也可能工作在中国；先识别当事人实际法律与生活所在地。欧洲不是单一劳动/离婚/医保制度，不允许统一写“欧盟规则适用于所有欧洲女性”。

### CN（简体中文大陆生活环境）P0
路径：职业婚育决策、赡养和照护、离婚财产证据、家庭关系边界、中年再就业、个人现金流、小微创业与主播/MCN合同。
需核来源：国家法律法规数据库、最高人民法院公布的司法解释与案例、人社部与各省市政务服务、国家医保局及地方医保、国家卫健委、国家统计局；核实地方落地及生效日期。
特殊：户籍/社保缴费地/实际居住地、房屋登记/婚前婚后取得、彩礼/赡养的争议事实、政策地域差、强亲属压力。禁止全国统一肯定性法律答案。

### US（美国）P0
路径：workplace discrimination / pay negotiation / career pivot, fertility/work tradeoff, childcare, divorce/co-parenting, housing security, credit/debt, eldercare, immigration-sensitive choices.
需核来源：EEOC、DOL、CFPB、IRS、HHS、state courts + local legal aid、州政府、官方health plans；FMLA 和州带薪假各有资格差异；在假设条件不齐时只讲要核实哪些条款。
特殊：联邦与州分层、雇员/1099承包商、雇主医疗保险和育儿成本、无偿照护、税后现金流、身份/签证依赖风险。不鼓励无证移民披露隐私。

### UK（英国）P0
路径：parental leave, employment rights, divorce finance, cohabitation, caregiving & benefits, NHS waiting and private alternatives, midlife career.
需核来源：GOV.UK、ACAS、Citizens Advice、NHS、legislation.gov.uk；英格兰/威尔士/苏格兰/北爱在多个问题上规则不同。
特殊：法定与雇主政策区分、福利资格、养老金/退休安排、住房产权、近亲照护成本。

### DE/FR（德国/法国）P1
路径：parental protections, childcare, part-time career tracks, social insurance, pension gaps, divorce/cohabitation property regimes, cross-border move.
需核来源：德国联邦政府及 Bundesministerium 官方门户、德国法院/州；法国 service-public.fr、Legifrance、劳动与家庭政府机构。欧盟官方 EUR-Lex 只说明欧盟层面的内容，具体资格还需成员国核实。
特殊：德国联邦/州规定及保险属性、法国就业类别和地区补助、跨境税和养老社保转移、非公民身份。
不得把美英样板直接套到德法；待本地审阅之前不得发布“权利速查结论”。

## locale fact卡 schema（每条一张）
```yaml
id: CN-LABOR-0001
jurisdiction: CN-SHENZHEN
topic: employment
statement: "待官方核查的具体权利/资格描述"
eligibility_conditions: []
exceptions: []
effective_from: null
verified_at: null
official_sources: []
status: NEEDS_VERIFICATION # VERIFIED / NEEDS_VERIFICATION / EXPIRED / CONFLICT
owner: null
reviewer: null
last_reviewed: null
```
对尚未核实事项不得在面向用户的答案中表达为确定性法律结论。法规事实引用应包括发布日期/更新日期及检索日期，关键问题注明“可能因所在地和个人情况不同”。

## 案例覆盖策略（不把名人成功当大众样本）
基准样本 22 篇继续保留研究用途。新增普通女性的匿名合成“决策场景”不冒充真实发生；若做真人匿名访谈，须同意、去标识化和证据链。优先按【生活困境类型×资源约束×地区】扩充到每类正反例，而不是 50 个名人名字。
人群覆盖：20s/30s/40s/50s/60+、未育/已育/不婚/单亲、城市/农村、低/中/高收入、残障、创业/职员/照护者、移民与非移民等。任何分组都不得将刻板印象作为个人结论。

## 版本与可维护性
每个 locale pack 有 owner / local reviewer / verified_at / official_sources / next_review_due。每次区域政策更新走 PR，附差异和测试样本，过期内容自动降级为 NEEDS_VERIFICATION。沉淀到案例素材库前做授权、引用、隐私和经济价值审核。