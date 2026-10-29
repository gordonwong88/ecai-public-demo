"""EC-AI Stage 1-F.1 visual demo v0.29 F2B layout correction evidence-driven relationship intelligence.
Synthetic, read-only narrative. No application or DB imports. F2 portfolio embedded.
Run standalone: streamlit run ecai_f2b_demo_v029.py
Import to existing app: from ecai_f2b_demo_v028 import render_demo
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from html import escape
import json

NAVY = '#071B3A'
INK = '#16283E'
BLUE = '#245D97'
TEAL = '#138779'
GOLD = '#BA8132'

CSS = '''<style>
/* Keep the banner BELOW the Streamlit app header; avoid top-edge clipping. */
[data-testid="stMainBlockContainer"]{padding-top:2.7rem !important;}
@media(max-width:750px){[data-testid="stMainBlockContainer"]{padding-top:2.7rem !important;}}
.f20-banner{background:linear-gradient(112deg,#071B3A 0%,#103C64 100%);border-radius:18px;padding:19px 24px 16px;margin:4px 0 4px;border:1px solid #1C4875;box-sizing:border-box;overflow:visible;min-height:142px}
.f20-eyebrow{color:#A9C7E6;letter-spacing:.13em;font-weight:850;font-size:11px}
.f20-head{color:white;font-size:30px;letter-spacing:-.025em;font-weight:900;margin:6px 0 6px;line-height:1.16}
.f20-sub{color:#D7E7F5;font-size:14px;line-height:1.4;max-width:870px}
.f20-demo-tag{display:inline-block;border:1px solid #688CAE;background:#153B62;padding:5px 11px;color:#E7F1FB;border-radius:30px;font-size:11px;font-weight:800;margin-top:3px}
.f20-panel{background:#fff;border:1px solid #DCE4ED;border-radius:14px;padding:14px 16px;margin:6px 0;box-shadow:0 3px 12px rgba(7,27,58,.035)}
.f20-small{font-size:11px;font-weight:850;letter-spacing:.1em;color:#34638C}
.f20-panel-head{font-size:20px;color:#071B3A;font-weight:850;margin:4px 0}
.f20-body{font-size:14px;line-height:1.6;color:#4B6076}
.f20-metric{background:#F6F9FC;border:1px solid #DCE4ED;border-radius:14px;padding:13px 14px;min-height:100px;box-sizing:border-box}
.f20-metric-label{color:#5C7185;font-size:12px;font-weight:800}
.f20-metric-value{color:#071B3A;font-weight:900;font-size:25px;margin-top:2px}
.f20-metric-note{color:#63788B;font-size:11px;margin-top:3px}
div.stButton > button[kind="primary"]{background:#164878;border-color:#164878;color:#fff}
.f21-decision{background:#F4F8FD;border-left:4px solid #245D97;padding:16px 19px;border-radius:8px;margin:8px 0 10px;color:#163454}
.f21-decision strong{color:#071B3A}
.f21-table{width:100%;border-collapse:collapse;font-size:13px;margin:6px 0 10px;border:1px solid #DCE4ED}
.f21-table th{background:#EFF4F9;color:#274867;text-align:left;padding:9px;border-bottom:1px solid #DCE4ED;font-size:12px}
.f21-table td{padding:9px;color:#2D455C;border-bottom:1px solid #E4EBF1;vertical-align:top}
.f21-table tr:nth-child(even){background:#F9FBFD}
.f21-pill{display:inline-block;padding:3px 9px;border-radius:20px;background:#E8EFF8;color:#164878;font-size:11px;font-weight:700}
/* Do not override Streamlit global vertical/horizontal block gaps: doing so caused overlapping widgets in v0.28. */
/* Preserve banner clearance on short viewports; shrink whitespace instead of clipping. */
@media(max-height:800px){[data-testid="stMainBlockContainer"]{padding-top:2.55rem !important;}}
/* Keep Streamlit's native Plotly widget margins to prevent panels colliding. */
.f2-evidence{border:1px solid #DCE4ED;border-radius:12px;background:#FFFFFF;overflow:hidden}
.f2-evidence table{border-collapse:collapse;width:100%;font-size:13px}
.f2-evidence th{text-align:left;width:29%;padding:8px 12px;color:#3A6285;background:#F6F9FC;border-bottom:1px solid #EBF0F5;font-size:11px;letter-spacing:.04em}
.f2-evidence td{padding:8px 12px;color:#193653;border-bottom:1px solid #EBF0F5}
.f20-caveat{font-size:11px;color:#65778A;border-left:3px solid #BACBD9;padding-left:10px;margin:3px 0}
@media (max-width:750px){.f20-banner{padding:24px 20px;min-height:0}.f20-head{font-size:25px}}

/* F5A.1: Scene-2 only: concise evidence grid. Do not tighten global Streamlit widget spacing. */
.f5-evidence-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px 10px;margin:4px 0 0}
.f5-evidence-cell{border:1px solid #E0E8F0;background:#F8FAFC;border-radius:8px;padding:7px 11px;min-width:0}
.f5-evidence-label{font-size:10px;font-weight:850;letter-spacing:.06em;color:#436381;margin-bottom:3px}
.f5-evidence-value{font-size:12px;line-height:1.35;color:#173553;overflow-wrap:anywhere}
.f5-source-note{font-size:10px;line-height:1.35;color:#667A8E;margin:5px 0 0}
@media(max-width:760px){.f5-evidence-grid{grid-template-columns:1fr}}
</style>'''
F2_DATA = json.loads('{"dataset_version":"F2.0","synthetic":true,"no_real_customer_data":true,"notes":["Scores are editorial test fixtures and are not calculated by the E5 engine.","Only Northstar has a financial proxy; blank fields are not zero.","Events are invented, not verified external facts.","The demo currently displays 4 management priorities, which is an editorial agenda count, not the number of ACT_NOW-quadrant dots."],"relationships":[{"relationship_id":"NSTAR","relationship":"Northstar Mobility","attention_score":82,"urgency_score":87,"management_category":"Growth","proposed_action":"Lending wallet expansion","forecast_capex_usdm":4000,"assumed_debt_funding_pct":25,"assumed_bank_funding_pct":60,"fictional_event":"CAPEX financing review","illustrative_review_window":"2027-Q1","proposed_owner":"Coverage","evidence_to_validate":"Validate CAPEX, debt mix and lender participation","confidence":"HIGH","evidence_type":"ASSUMPTION","priority_quadrant":"ACT_NOW","lending_proxy_usdm":600.0,"source_status":"FICTIONAL_DEMO_NOT_SOURCED","persisted":false},{"relationship_id":"HLINE","relationship":"Harbourline Energy","attention_score":73,"urgency_score":68,"management_category":"Relationship","proposed_action":"Deposit retention","forecast_capex_usdm":null,"assumed_debt_funding_pct":null,"assumed_bank_funding_pct":null,"fictional_event":"Hypothetical treasury mandate review","illustrative_review_window":"2026-Q4","proposed_owner":"Treasury","evidence_to_validate":"Confirm deposit maturity ladder and expected outflows","confidence":"MEDIUM","evidence_type":"ASSUMPTION","priority_quadrant":"ACT_NOW","lending_proxy_usdm":null,"source_status":"FICTIONAL_DEMO_NOT_SOURCED","persisted":false},{"relationship_id":"SUMMIT","relationship":"Summit Infrastructure","attention_score":65,"urgency_score":59,"management_category":"Risk","proposed_action":"Credit review","forecast_capex_usdm":null,"assumed_debt_funding_pct":null,"assumed_bank_funding_pct":null,"fictional_event":"Illustrative covenant monitoring window","illustrative_review_window":"2026-Q4","proposed_owner":"Credit / Risk","evidence_to_validate":"Validate covenant headroom and maturity schedule","confidence":"MEDIUM","evidence_type":"ASSUMPTION","priority_quadrant":"ACT_NOW","lending_proxy_usdm":null,"source_status":"FICTIONAL_DEMO_NOT_SOURCED","persisted":false},{"relationship_id":"MERID","relationship":"Meridian Logistics","attention_score":56,"urgency_score":75,"management_category":"Relationship","proposed_action":"Coverage enhancement","forecast_capex_usdm":null,"assumed_debt_funding_pct":null,"assumed_bank_funding_pct":null,"fictional_event":"Hypothetical overseas expansion announcement","illustrative_review_window":"2026-Q4","proposed_owner":"Coverage","evidence_to_validate":"Confirm event and coverage ownership","confidence":"MEDIUM","evidence_type":"ASSUMPTION","priority_quadrant":"HIGH_URGENCY","lending_proxy_usdm":null,"source_status":"FICTIONAL_DEMO_NOT_SOURCED","persisted":false},{"relationship_id":"BLUE","relationship":"Bluecrest Digital","attention_score":69,"urgency_score":33,"management_category":"Growth","proposed_action":"Treasury deep dive","forecast_capex_usdm":null,"assumed_debt_funding_pct":null,"assumed_bank_funding_pct":null,"fictional_event":"Hypothetical operating cash increase","illustrative_review_window":"2027-Q1","proposed_owner":"Treasury","evidence_to_validate":"Validate operating cash and serviceable liquidity","confidence":"LOW","evidence_type":"ASSUMPTION","priority_quadrant":"HIGH_ATTENTION","lending_proxy_usdm":null,"source_status":"FICTIONAL_DEMO_NOT_SOURCED","persisted":false},{"relationship_id":"WEST","relationship":"Westbridge Consumer","attention_score":52,"urgency_score":36,"management_category":"Strategic","proposed_action":"Portfolio monitoring","forecast_capex_usdm":null,"assumed_debt_funding_pct":null,"assumed_bank_funding_pct":null,"fictional_event":"Illustrative trading update","illustrative_review_window":"2027-Q1","proposed_owner":"Portfolio Strategy","evidence_to_validate":"Revisit next review if signal changes","confidence":"LOW","evidence_type":"ASSUMPTION","priority_quadrant":"MONITOR","lending_proxy_usdm":null,"source_status":"FICTIONAL_DEMO_NOT_SOURCED","persisted":false},{"relationship_id":"ATLAS","relationship":"Atlas Renewables","attention_score":44,"urgency_score":62,"management_category":"Risk","proposed_action":"Financing event review","forecast_capex_usdm":null,"assumed_debt_funding_pct":null,"assumed_bank_funding_pct":null,"fictional_event":"Hypothetical refinancing calendar","illustrative_review_window":"2026-Q4","proposed_owner":"Coverage","evidence_to_validate":"Confirm refinancing dates and funding need","confidence":"MEDIUM","evidence_type":"ASSUMPTION","priority_quadrant":"HIGH_URGENCY","lending_proxy_usdm":null,"source_status":"FICTIONAL_DEMO_NOT_SOURCED","persisted":false},{"relationship_id":"STER","relationship":"Sterling Healthcare","attention_score":38,"urgency_score":30,"management_category":"Strategic","proposed_action":"Portfolio monitoring","forecast_capex_usdm":null,"assumed_debt_funding_pct":null,"assumed_bank_funding_pct":null,"fictional_event":"No material simulated event","illustrative_review_window":"2027-Q1","proposed_owner":"Portfolio Strategy","evidence_to_validate":"Maintain routine monitoring","confidence":"LOW","evidence_type":"ASSUMPTION","priority_quadrant":"MONITOR","lending_proxy_usdm":null,"source_status":"FICTIONAL_DEMO_NOT_SOURCED","persisted":false},{"relationship_id":"CALD","relationship":"Caldera Industrials","attention_score":59,"urgency_score":42,"management_category":"Growth","proposed_action":"Cross-border expansion","forecast_capex_usdm":null,"assumed_debt_funding_pct":null,"assumed_bank_funding_pct":null,"fictional_event":"Hypothetical subsidiary establishment","illustrative_review_window":"2027-Q1","proposed_owner":"Cross-border Coverage","evidence_to_validate":"Validate entity structure and banking needs","confidence":"LOW","evidence_type":"ASSUMPTION","priority_quadrant":"MONITOR","lending_proxy_usdm":null,"source_status":"FICTIONAL_DEMO_NOT_SOURCED","persisted":false},{"relationship_id":"ORION","relationship":"Orion Shipping","attention_score":42,"urgency_score":46,"management_category":"Relationship","proposed_action":"Coverage enhancement","forecast_capex_usdm":null,"assumed_debt_funding_pct":null,"assumed_bank_funding_pct":null,"fictional_event":"Illustrative facility renewal","illustrative_review_window":"2027-Q1","proposed_owner":"Coverage","evidence_to_validate":"Confirm utilization and relationship coverage","confidence":"LOW","evidence_type":"ASSUMPTION","priority_quadrant":"MONITOR","lending_proxy_usdm":null,"source_status":"FICTIONAL_DEMO_NOT_SOURCED","persisted":false}]}')
RELATIONSHIPS = F2_DATA['relationships']
REL_BY_NAME = {r['relationship']: r for r in RELATIONSHIPS}

SCENES = ('Executive Briefing', 'Wallet Intelligence', 'Attention × Urgency', 'Management Decision', 'Execution & Outcome')


def _panel(kicker, title, body):
    st.markdown(f'<div class="f20-panel"><div class="f20-small">{kicker}</div><div class="f20-panel-head">{title}</div><div class="f20-body">{body}</div></div>', unsafe_allow_html=True)


def _metric(label, val, note):
    st.markdown(f'<div class="f20-metric"><div class="f20-metric-label">{label}</div><div class="f20-metric-value">{val}</div><div class="f20-metric-note">{note}</div></div>', unsafe_allow_html=True)


def _selected_relationship():
    if 'f2_selected' not in st.session_state or st.session_state.f2_selected not in REL_BY_NAME:
        st.session_state.f2_selected = 'Northstar Mobility'
    return REL_BY_NAME[st.session_state.f2_selected]


def _relationship_selector():
    st.selectbox('Relationship focus · synthetic', list(REL_BY_NAME), key='f2_selected',
                 help='Demo-only relationship selection; not saved to any database.')
    return _selected_relationship()


def _evidence_panel(r):
    """Compact six-field, two-column grid for Scene 2, preserving all synthetic evidence."""
    capex = r.get('forecast_capex_usdm')
    if capex is None:
        proxy = 'Not estimated — financial inputs unavailable'
    else:
        proxy = ('USD {:,.0f}m illustrative notional proxy'.format(r['lending_proxy_usdm'])
                 if r.get('lending_proxy_usdm') is not None else 'Not estimated')
    entries = [
        ('MANAGEMENT SIGNAL', f"{r['management_category']} · {r['proposed_action']}"),
        ('ATTENTION × URGENCY', f"{r['attention_score']} × {r['urgency_score']} · {r['priority_quadrant'].replace('_',' ')}"),
        ('FICTIONAL EVENT', r['fictional_event']),
        ('EVIDENCE TO VALIDATE', r['evidence_to_validate']),
        ('ACCOUNTABLE FUNCTION', r['proposed_owner']),
        ('FINANCIAL EVIDENCE', proxy),
    ]
    cells = ''.join(
        '<div class="f5-evidence-cell"><div class="f5-evidence-label">'+escape(str(k))+'</div>'
        '<div class="f5-evidence-value">'+escape(str(v))+'</div></div>'
        for k,v in entries
    )
    st.markdown('<div class="f5-evidence-grid">'+cells+'</div>'
                '<div class="f5-source-note">Evidence type: ASSUMPTION · Source: FICTIONAL DEMO, NOT SOURCED · '
                'Confidence: editorial fixture, not verified fact</div>',unsafe_allow_html=True)


def _scatter():
    # Intentionally authored synthetic scores, not calculated from live records.
    frame = pd.DataFrame([{
        'Relationship': r['relationship'], 'Attention': r['attention_score'],
        'Urgency': r['urgency_score'], 'Marker': 33 if r['relationship']=='Northstar Mobility' else (25 if r['priority_quadrant']=='ACT_NOW' else 16),
        'Action': r['proposed_action']
    } for r in RELATIONSHIPS])
    fig = go.Figure()
    fig.add_shape(type='rect', x0=61, x1=100, y0=50, y1=100, fillcolor='rgba(186,129,50,.09)', line_width=0)
    fig.add_vline(x=61, line_dash='dash', line_color='#B2C0CE')
    fig.add_hline(y=50, line_dash='dash', line_color='#B2C0CE')
    # Label only the lead case by default. Other relationships remain discoverable via hover.
    fig.add_trace(go.Scatter(x=frame['Attention'],y=frame['Urgency'], mode='markers',
                             marker=dict(size=frame['Marker'],color=[GOLD if x>=61 and y>=50 else BLUE for x,y in zip(frame.Attention, frame.Urgency)],
                                         opacity=.9,line=dict(color='white',width=2)),
                             customdata=frame[['Relationship','Action']].to_numpy(),
                             hovertemplate='<b>%{customdata[0]}</b><br>Attention: %{x}<br>Urgency: %{y}<br>Illustrative action: %{customdata[1]}<extra></extra>'))
    fig.add_annotation(x=82,y=87,text='<b>Northstar Mobility</b>',showarrow=True,arrowhead=0,ax=-95,ay=-27,
                       bgcolor='rgba(255,255,255,.95)',bordercolor='#DCE4ED',borderpad=5,font=dict(color=NAVY,size=11))
    fig.add_annotation(x=96,y=96,text='ACT NOW',showarrow=False,xanchor='right',font=dict(color='#8A5B1D',size=12))
    fig.update_layout(height=290,showlegend=False,margin=dict(t=20,b=26,l=30,r=10),paper_bgcolor='white',plot_bgcolor='white',
                      xaxis=dict(title='Management attention',range=[20,100],gridcolor='#ECF0F4',zeroline=False),
                      yaxis=dict(title='Urgency',range=[10,100],gridcolor='#ECF0F4',zeroline=False))
    st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})


def render_demo():
    """Render synthetic demo only; this function never reads or writes a database."""
    st.markdown(CSS,unsafe_allow_html=True)
    # Public showcase: deliberately no links to internal/test/production workspaces.
    # All values remain synthetic in-process fixtures; no database or API clients.
    st.markdown('''<div class="f20-banner">
    <div class="f20-eyebrow">EC-AI / INSTITUTIONAL RELATIONSHIP INTELLIGENCE</div>
    <div class="f20-head">Portfolio intelligence. Clear executive decisions.</div>
    <div class="f20-sub">Identify portfolio priorities, understand the evidence, make the decision, and track accountability — in one executive workflow.</div>
    <div class="f20-demo-tag">FICTIONAL DEMO · 10 SYNTHETIC RELATIONSHIPS · READ-ONLY</div></div>''',unsafe_allow_html=True)
    if 'f20_scene' not in st.session_state:
        st.session_state.f20_scene=0
    step=int(st.session_state.f20_scene)
    nav=st.columns(5,gap='small')
    for i,(c,label) in enumerate(zip(nav,SCENES)):
        with c:
            if st.button(f'{i+1} · {label}',key=f'f20_nav_{i}',type='primary' if i==step else 'secondary',use_container_width=True):
                st.session_state.f20_scene=i
                st.rerun()
    st.progress((step+1)/5)
    # Native Streamlit block separation; never push content over preceding widgets.
    if step==0:
        a,b,c,d=st.columns(4)
        with a:_metric('Relationships','10','Synthetic portfolio')
        with b:_metric('Management priorities','4','Illustrative signals')
        with c:_metric('Lead lending proxy','USD 600m','Not a financing commitment')
        with d:_metric('Decision to consider','1','Authorize diligence only')
        left,right=st.columns([1.65,1],gap='large')
        with left:_scatter()
        with right:
            _panel('EXECUTIVE INTERPRETATION','Northstar Mobility requires attention',
                   'The largest illustrative opportunity coincides with a fictional near-term financing milestone. The executive needs to decide whether a structured wallet review is warranted.')
            _panel('THIS WEEK’S AGENDA','From insight to management action',
                   'Investigate Northstar financing needs; review a hypothetical deposit-retention exposure; assess a fictional credit event; confirm coverage of a cross-border opportunity.')
    elif step==1:
        r = _relationship_selector()
        if r['relationship']=='Northstar Mobility':
            a,b,c,d=st.columns(4)
            with a:_metric('Forecast CAPEX','USD 4.0bn','Synthetic assumption')
            with b:_metric('Assumed debt funding','25%','Illustrative proxy')
            with c:_metric('Assumed bank funding','60%','Illustrative proxy')
            with d:_metric('Addressable notional','USD 600m','Not revenue or wallet share')
            _panel('EXPLAINABLE FINANCIAL INTELLIGENCE','USD 4,000m × 25% × 60% = USD 600m',
                   'An illustrative lending notional proxy, not expected revenue, market wallet share, a mandate or committed exposure.')
        else:
            _panel('FINANCIAL EVIDENCE UNAVAILABLE','No financial proxy estimated',
                   'The source dataset intentionally contains no financial inputs for this relationship. Unknown is not zero, and no opportunity amount is inferred.')
        _evidence_panel(r)
    elif step==2:
        r = _relationship_selector()
        left,right=st.columns([1.65,1],gap='large')
        with left:_scatter()
        with right:
            _panel('SELECTED RELATIONSHIP',escape(r['relationship']),
                   f"{escape(r['management_category'])} · {escape(r['proposed_action'])}. "
                   f"Illustrative attention {r['attention_score']} and urgency {r['urgency_score']}. "
                   'Scores are editorial demonstration fixtures, not the governed E5 model.')
            _panel('WHY REVIEW?',escape(r['fictional_event']),escape(r['evidence_to_validate']))
            st.caption('Recommendation: management review only. No executive authorization or system write.')
    elif step==3:
        st.caption('Lead decision case: Northstar Mobility · selection on Scenes 2–3 does not change this scenario.')
        _panel('DECISION REQUIRED','Authorize diligence, not lending',
               'Northstar Mobility: validate the USD 600m illustrative lending proxy before making any financing or capital-allocation commitment.')
        choice=st.radio('Select an illustrative management disposition',
                        ['Approve investigation','Modify scope','Defer pending evidence'],key='f20_decision',horizontal=True)
        text={
            'Approve investigation': ('APPROVE SCOPED INVESTIGATION', 'Request Coverage, Treasury and Credit assessments. No facility approval or client commitment.'),
            'Modify scope': ('MODIFY INVESTIGATION SCOPE', 'Prioritize Coverage validation and Treasury discovery; defer Credit work until core facts are confirmed.'),
            'Defer pending evidence': ('DEFER — NO EXECUTION AUTHORIZED', 'Request a better-sourced CAPEX forecast and financing timetable before considering an investigation.')
        }
        title,description=text[choice]
        st.markdown(f'<div class="f21-decision"><strong>{escape(title)}</strong><div>{escape(description)}</div></div>',unsafe_allow_html=True)
        a,b,c=st.columns(3)
        with a:_metric('Decision authority','Executive','Illustrative choice only')
        with b:_metric('Evidence quality','Assumptions','Needs independent validation')
        with c:_metric('Write operations','None','No operational records')
        st.caption('This selection affects only Scene 5 in this browser session; it is not a saved Decision.')
    else:
        choice=st.session_state.get('f20_decision','Approve investigation')
        st.markdown('**Illustrative execution plan — Northstar Mobility lead case**')
        if choice=='Defer pending evidence':
            st.info('Decision deferred. No execution actions are authorized. The items below are evidence requests for reconsideration, not activated ExecutionActions.')
            rows=[
              ('Coverage','Obtain a reliable CAPEX forecast and projected financing timetable','Before next review','Evidence request'),
              ('Portfolio Strategy','Assess completeness and source quality of available financial assumptions','Before next review','Evidence request')]
        elif choice=='Modify scope':
            st.info('Modified scope: only Coverage and Treasury discovery are proposed. Credit engagement is held until core evidence is available.')
            rows=[
              ('Relationship Coverage','Confirm client financing objectives and access','Next review','Proposed'),
              ('Treasury','Screen liquidity and deposit adjacency','Next review','Proposed')]
        else:
            st.info('Investigation approved for discussion only. These fictional actions are proposed; no database execution records have been created.')
            rows=[
              ('Relationship Coverage','Validate financing need, expected timing and client access','Next review','Proposed'),
              ('Treasury','Assess deposits, cash and liquidity adjacency','Next review','Proposed'),
              ('Credit / Risk','Review preliminary suitability and key risk considerations','Following review','Proposed'),
              ('Executive sponsor','Evaluate evidence and decide pursue / defer / close','Following review','Proposed')]
        body=''.join('<tr><td>'+'</td><td>'.join(escape(str(x)) for x in row[:3])+'</td><td><span class="f21-pill">'+escape(row[3])+'</span></td></tr>' for row in rows)
        st.markdown('<table class="f21-table"><thead><tr><th>ACCOUNTABLE FUNCTION</th><th>ILLUSTRATIVE NEXT STEP</th><th>REVIEW POINT</th><th>STATE</th></tr></thead><tbody>'+body+'</tbody></table>',unsafe_allow_html=True)
        _panel('EXPECTED OUTCOME','Decision accountability, not dashboard activity',
               'At the next executive review: identify which assumptions were verified, which relationship opportunity remains credible, and what leadership should decide next.')
    st.markdown('<div class="f20-caveat">All relationships, scores, financial values, events and responsibilities above are fictional. This demo does not access, update or publish operational records.</div>',unsafe_allow_html=True)
    prev,_,nxt=st.columns([1,3,1])
    with prev:
        if st.button('← Previous',disabled=step==0,key='f20_prev',use_container_width=True):
            st.session_state.f20_scene=step-1;st.rerun()
    with nxt:
        if st.button('Next →',disabled=step==4,key='f20_next',use_container_width=True):
            st.session_state.f20_scene=step+1;st.rerun()


if __name__=='__main__':
    st.set_page_config(page_title='EC-AI — Executive Intelligence Demo',page_icon='🏦',layout='wide')
    render_demo()
