import os
import subprocess
from pathlib import Path

BASE_DIR = Path(r"c:\Users\MyPC\3RDYR-CS\rrscraper")
DRAWIO_PATH = BASE_DIR / "MACADANGDANG_ERD.drawio"
HTML_PATH = BASE_DIR / "MACADANGDANG_ERD.html"
PDF_PATH = BASE_DIR / "MACADANGDANG_ERD.pdf"

# 1. DRAW.IO NATIVE DIAGRAM XML
drawio_content = """<mxfile host="app.diagrams.net" modified="2026-09-21T11:50:00.000Z" agent="Mozilla/5.0" version="24.0.0" type="device">
  <diagram id="PhysicalERD_RRScraper" name="Physical ERD - Royal Road Scraper">
    <mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1650" pageHeight="950" background="#f8fafc" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Banner -->
        <mxCell id="title_banner" value="&lt;b style='font-size: 19px;'&gt;PHYSICAL ENTITY-RELATIONSHIP DIAGRAM (ERD)&lt;/b&gt;&lt;br&gt;&lt;span style='font-size: 13px; color: #475569;'&gt;&lt;b&gt;Proposed System:&lt;/b&gt; Royal Road Scraper &amp;amp; Web Fiction Tracker (rrscraper) &amp;nbsp;|&amp;nbsp; &lt;b&gt;Database Engine:&lt;/b&gt; PostgreSQL 17 (Supabase) &amp;nbsp;|&amp;nbsp; &lt;b&gt;Course:&lt;/b&gt; CSIT327 &amp;nbsp;|&amp;nbsp; &lt;b&gt;Student:&lt;/b&gt; Yoji Macadangdang&lt;/span&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#cbd5e1;strokeWidth=1.5;arcSize=6;shadow=1;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="40" y="20" width="1520" height="65" as="geometry" />
        </mxCell>

        <!-- TABLE: auth_user -->
        <mxCell id="t_auth_user" value="auth_user" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;fillColor=#0f172a;fontColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;shadow=1;rounded=1;arcSize=6;" vertex="1" parent="1">
          <mxGeometry x="40" y="110" width="300" height="294" as="geometry" />
        </mxCell>
        <mxCell id="c_u_id" value="PK | id : INTEGER" style="text;strokeColor=none;fillColor=#fee2e2;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#b91c1c;" vertex="1" parent="t_auth_user">
          <mxGeometry y="30" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_u_username" value="UQ | username : VARCHAR(150) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#0f172a;fontStyle=1;" vertex="1" parent="t_auth_user">
          <mxGeometry y="54" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_u_email" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| email : VARCHAR(254) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_auth_user">
          <mxGeometry y="78" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_u_password" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| password : VARCHAR(128) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_auth_user">
          <mxGeometry y="102" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_u_first_name" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| first_name : VARCHAR(150)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_auth_user">
          <mxGeometry y="126" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_u_last_name" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| last_name : VARCHAR(150)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_auth_user">
          <mxGeometry y="150" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_u_is_active" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| is_active : BOOLEAN [DF: true]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_auth_user">
          <mxGeometry y="174" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_u_is_staff" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| is_staff : BOOLEAN [DF: false]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_auth_user">
          <mxGeometry y="198" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_u_is_superuser" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| is_superuser : BOOLEAN [DF: false]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_auth_user">
          <mxGeometry y="222" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_u_date_joined" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| date_joined : TIMESTAMPTZ [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_auth_user">
          <mxGeometry y="246" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_u_last_login" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| last_login : TIMESTAMPTZ" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_auth_user">
          <mxGeometry y="270" width="300" height="24" as="geometry" />
        </mxCell>

        <!-- TABLE: profile_profile -->
        <mxCell id="t_profile" value="profile_profile" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;fillColor=#0f172a;fontColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;shadow=1;rounded=1;arcSize=6;" vertex="1" parent="1">
          <mxGeometry x="40" y="440" width="300" height="150" as="geometry" />
        </mxCell>
        <mxCell id="c_prof_id" value="PK | id : BIGINT" style="text;strokeColor=none;fillColor=#fee2e2;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#b91c1c;" vertex="1" parent="t_profile">
          <mxGeometry y="30" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_prof_uid" value="FK | user_id : INTEGER [UQ, NN]" style="text;strokeColor=none;fillColor=#dbeafe;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#1d4ed8;" vertex="1" parent="t_profile">
          <mxGeometry y="54" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_prof_fn" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| full_name : VARCHAR(150)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_profile">
          <mxGeometry y="78" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_prof_bio" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| bio : TEXT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_profile">
          <mxGeometry y="102" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_prof_img" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| profile_image : VARCHAR(100)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_profile">
          <mxGeometry y="126" width="300" height="24" as="geometry" />
        </mxCell>

        <!-- TABLE: user_settings_usersettings -->
        <mxCell id="t_settings" value="user_settings_usersettings" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;fillColor=#0f172a;fontColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;shadow=1;rounded=1;arcSize=6;" vertex="1" parent="1">
          <mxGeometry x="40" y="630" width="300" height="126" as="geometry" />
        </mxCell>
        <mxCell id="c_set_id" value="PK | id : BIGINT" style="text;strokeColor=none;fillColor=#fee2e2;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#b91c1c;" vertex="1" parent="t_settings">
          <mxGeometry y="30" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_set_uid" value="FK | user_id : INTEGER [UQ, NN]" style="text;strokeColor=none;fillColor=#dbeafe;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#1d4ed8;" vertex="1" parent="t_settings">
          <mxGeometry y="54" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_set_dm" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| dark_mode : BOOLEAN [DF: false]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_settings">
          <mxGeometry y="78" width="300" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_set_en" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| email_notifications : BOOLEAN [DF: true]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_settings">
          <mxGeometry y="102" width="300" height="24" as="geometry" />
        </mxCell>

        <!-- TABLE: scraper_job -->
        <mxCell id="t_scraper_job" value="scraper_job" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;fillColor=#0f172a;fontColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;shadow=1;rounded=1;arcSize=6;" vertex="1" parent="1">
          <mxGeometry x="390" y="110" width="320" height="246" as="geometry" />
        </mxCell>
        <mxCell id="c_job_id" value="PK | id : BIGINT" style="text;strokeColor=none;fillColor=#fee2e2;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#b91c1c;" vertex="1" parent="t_scraper_job">
          <mxGeometry y="30" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_job_uid" value="FK | user_id : INTEGER [NN]" style="text;strokeColor=none;fillColor=#dbeafe;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#1d4ed8;" vertex="1" parent="t_scraper_job">
          <mxGeometry y="54" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_job_nid" value="FK | novel_id : BIGINT [NULL]" style="text;strokeColor=none;fillColor=#dbeafe;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#1d4ed8;" vertex="1" parent="t_scraper_job">
          <mxGeometry y="78" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_job_url" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| target_url : VARCHAR(500) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_scraper_job">
          <mxGeometry y="102" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_job_st" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| status : VARCHAR(30) [DF: 'PENDING']" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_scraper_job">
          <mxGeometry y="126" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_job_cs" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| chapters_scraped : INTEGER [DF: 0]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_scraper_job">
          <mxGeometry y="150" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_job_err" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| error_message : TEXT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_scraper_job">
          <mxGeometry y="174" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_job_start" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| started_at : TIMESTAMPTZ [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_scraper_job">
          <mxGeometry y="198" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_job_end" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| completed_at : TIMESTAMPTZ" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_scraper_job">
          <mxGeometry y="222" width="320" height="24" as="geometry" />
        </mxCell>

        <!-- TABLE: tracker_bookmark -->
        <mxCell id="t_bookmark" value="tracker_bookmark" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;fillColor=#0f172a;fontColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;shadow=1;rounded=1;arcSize=6;" vertex="1" parent="1">
          <mxGeometry x="390" y="390" width="320" height="246" as="geometry" />
        </mxCell>
        <mxCell id="c_bm_id" value="PK | id : BIGINT" style="text;strokeColor=none;fillColor=#fee2e2;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#b91c1c;" vertex="1" parent="t_bookmark">
          <mxGeometry y="30" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_bm_uid" value="FK | user_id : INTEGER [NN]" style="text;strokeColor=none;fillColor=#dbeafe;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#1d4ed8;" vertex="1" parent="t_bookmark">
          <mxGeometry y="54" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_bm_nid" value="FK | novel_id : BIGINT [NN]" style="text;strokeColor=none;fillColor=#dbeafe;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#1d4ed8;" vertex="1" parent="t_bookmark">
          <mxGeometry y="78" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_bm_cid" value="FK | last_read_chapter_id : BIGINT [NULL]" style="text;strokeColor=none;fillColor=#dbeafe;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#1d4ed8;" vertex="1" parent="t_bookmark">
          <mxGeometry y="102" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_bm_rs" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| reading_status : VARCHAR(30) [DF: 'READING']" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_bookmark">
          <mxGeometry y="126" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_bm_fav" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| is_favorite : BOOLEAN [DF: false]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_bookmark">
          <mxGeometry y="150" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_bm_lra" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| last_read_at : TIMESTAMPTZ [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_bookmark">
          <mxGeometry y="174" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_bm_ca" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| created_at : TIMESTAMPTZ [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_bookmark">
          <mxGeometry y="198" width="320" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_bm_uq" value="UQ | UNIQUE(user_id, novel_id)" style="text;strokeColor=none;fillColor=#d1fae5;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=2;fontColor=#047857;" vertex="1" parent="t_bookmark">
          <mxGeometry y="222" width="320" height="24" as="geometry" />
        </mxCell>

        <!-- TABLE: scraper_novel -->
        <mxCell id="t_novel" value="scraper_novel" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;fillColor=#0f172a;fontColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;shadow=1;rounded=1;arcSize=6;" vertex="1" parent="1">
          <mxGeometry x="780" y="140" width="330" height="318" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_id" value="PK | id : BIGINT" style="text;strokeColor=none;fillColor=#fee2e2;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#b91c1c;" vertex="1" parent="t_novel">
          <mxGeometry y="30" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_rrid" value="UQ | royalroad_id : VARCHAR(50) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#0f172a;fontStyle=1;" vertex="1" parent="t_novel">
          <mxGeometry y="54" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_title" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| title : VARCHAR(255) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_novel">
          <mxGeometry y="78" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_auth" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| author_name : VARCHAR(150) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_novel">
          <mxGeometry y="102" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_syn" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| synopsis : TEXT" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_novel">
          <mxGeometry y="126" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_img" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| cover_image_url : VARCHAR(500)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_novel">
          <mxGeometry y="150" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_st" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| status : VARCHAR(30) [DF: 'ONGOING']" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_novel">
          <mxGeometry y="174" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_rt" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| rating : NUMERIC(3,2)" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_novel">
          <mxGeometry y="198" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_tp" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| total_pages : INTEGER [DF: 0]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_novel">
          <mxGeometry y="222" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_src" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| source_url : VARCHAR(500) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_novel">
          <mxGeometry y="246" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_ca" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| created_at : TIMESTAMPTZ [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_novel">
          <mxGeometry y="270" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nov_ua" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| updated_at : TIMESTAMPTZ [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_novel">
          <mxGeometry y="294" width="330" height="24" as="geometry" />
        </mxCell>

        <!-- TABLE: scraper_chapter -->
        <mxCell id="t_chapter" value="scraper_chapter" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;fillColor=#0f172a;fontColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;shadow=1;rounded=1;arcSize=6;" vertex="1" parent="1">
          <mxGeometry x="1180" y="140" width="340" height="270" as="geometry" />
        </mxCell>
        <mxCell id="c_chap_id" value="PK | id : BIGINT" style="text;strokeColor=none;fillColor=#fee2e2;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#b91c1c;" vertex="1" parent="t_chapter">
          <mxGeometry y="30" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_chap_nid" value="FK | novel_id : BIGINT [NN]" style="text;strokeColor=none;fillColor=#dbeafe;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#1d4ed8;" vertex="1" parent="t_chapter">
          <mxGeometry y="54" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_chap_rrid" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| royalroad_chapter_id : VARCHAR(50) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_chapter">
          <mxGeometry y="78" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_chap_num" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| chapter_number : INTEGER [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_chapter">
          <mxGeometry y="102" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_chap_title" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| title : VARCHAR(255) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_chapter">
          <mxGeometry y="126" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_chap_cnt" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| content : TEXT [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_chapter">
          <mxGeometry y="150" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_chap_wc" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| word_count : INTEGER [DF: 0]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_chapter">
          <mxGeometry y="174" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_chap_url" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| source_url : VARCHAR(500) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_chapter">
          <mxGeometry y="198" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_chap_rel" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| release_date : TIMESTAMPTZ" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_chapter">
          <mxGeometry y="222" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_chap_sa" value="&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;| scraped_at : TIMESTAMPTZ [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#334155;" vertex="1" parent="t_chapter">
          <mxGeometry y="246" width="340" height="24" as="geometry" />
        </mxCell>

        <!-- TABLE: scraper_novel_tags (Junction) -->
        <mxCell id="t_novel_tags" value="scraper_novel_tags" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;fillColor=#0f172a;fontColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;shadow=1;rounded=1;arcSize=6;" vertex="1" parent="1">
          <mxGeometry x="780" y="520" width="330" height="130" as="geometry" />
        </mxCell>
        <mxCell id="c_nt_id" value="PK | id : BIGINT" style="text;strokeColor=none;fillColor=#fee2e2;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#b91c1c;" vertex="1" parent="t_novel_tags">
          <mxGeometry y="30" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nt_nid" value="FK | novel_id : BIGINT [NN]" style="text;strokeColor=none;fillColor=#dbeafe;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#1d4ed8;" vertex="1" parent="t_novel_tags">
          <mxGeometry y="54" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nt_tid" value="FK | tag_id : BIGINT [NN]" style="text;strokeColor=none;fillColor=#dbeafe;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#1d4ed8;" vertex="1" parent="t_novel_tags">
          <mxGeometry y="78" width="330" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_nt_uq" value="UQ | UNIQUE(novel_id, tag_id)" style="text;strokeColor=none;fillColor=#d1fae5;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=2;fontColor=#047857;" vertex="1" parent="t_novel_tags">
          <mxGeometry y="102" width="330" height="24" as="geometry" />
        </mxCell>

        <!-- TABLE: scraper_tag -->
        <mxCell id="t_tag" value="scraper_tag" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;html=1;fillColor=#0f172a;fontColor=#ffffff;strokeColor=#0f172a;strokeWidth=2;shadow=1;rounded=1;arcSize=6;" vertex="1" parent="1">
          <mxGeometry x="1180" y="520" width="340" height="106" as="geometry" />
        </mxCell>
        <mxCell id="c_tag_id" value="PK | id : BIGINT" style="text;strokeColor=none;fillColor=#fee2e2;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontStyle=1;fontColor=#b91c1c;" vertex="1" parent="t_tag">
          <mxGeometry y="30" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_tag_name" value="UQ | name : VARCHAR(50) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#0f172a;fontStyle=1;" vertex="1" parent="t_tag">
          <mxGeometry y="54" width="340" height="24" as="geometry" />
        </mxCell>
        <mxCell id="c_tag_slug" value="UQ | slug : VARCHAR(50) [NN]" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;spacingRight=8;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontColor=#0f172a;fontStyle=1;" vertex="1" parent="t_tag">
          <mxGeometry y="78" width="340" height="24" as="geometry" />
        </mxCell>

        <!-- RELATIONSHIP CONNECTIONS -->
        <!-- 1. auth_user -> profile_profile (1:1) -->
        <mxCell id="rel_u_p" value="1 : 1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmandOne;endFill=0;strokeWidth=2;strokeColor=#1d4ed8;fontStyle=1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="t_auth_user" target="t_profile">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 2. auth_user -> user_settings (1:1) -->
        <mxCell id="rel_p_s" value="1 : 1" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmandOne;endFill=0;strokeWidth=2;strokeColor=#1d4ed8;fontStyle=1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="t_profile" target="t_settings">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 3. auth_user -> scraper_job (1:N) -->
        <mxCell id="rel_u_j" value="1 : N" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;strokeWidth=2;strokeColor=#059669;fontStyle=1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="t_auth_user" target="t_scraper_job">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="365" y="200" />
              <mxPoint x="365" y="200" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 4. auth_user -> tracker_bookmark (1:N) -->
        <mxCell id="rel_u_bm" value="1 : N" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;strokeWidth=2;strokeColor=#059669;fontStyle=1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="t_auth_user" target="t_bookmark">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="365" y="340" />
              <mxPoint x="365" y="470" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 5. scraper_novel -> scraper_job (1:0..N) -->
        <mxCell id="rel_nov_j" value="1 : 0..N" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERzeroToMany;endFill=0;strokeWidth=2;strokeColor=#d97706;fontStyle=1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="t_novel" target="t_scraper_job">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="750" y="230" />
              <mxPoint x="750" y="230" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 6. scraper_novel -> tracker_bookmark (1:N) -->
        <mxCell id="rel_nov_bm" value="1 : N" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;strokeWidth=2;strokeColor=#d97706;fontStyle=1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="t_novel" target="t_bookmark">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="750" y="380" />
              <mxPoint x="750" y="470" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 7. scraper_novel -> scraper_chapter (1:N) -->
        <mxCell id="rel_nov_c" value="1 : N" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;strokeWidth=2;strokeColor=#dc2626;fontStyle=1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="t_novel" target="t_chapter">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1145" y="250" />
              <mxPoint x="1145" y="250" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- 8. scraper_novel -> scraper_novel_tags (1:N) -->
        <mxCell id="rel_nov_nt" value="1 : N" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;strokeWidth=2;strokeColor=#0891b2;fontStyle=1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="t_novel" target="t_novel_tags">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 9. scraper_tag -> scraper_novel_tags (1:N) -->
        <mxCell id="rel_tag_nt" value="1 : N" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERmany;endFill=0;strokeWidth=2;strokeColor=#0891b2;fontStyle=1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="t_tag" target="t_novel_tags">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- 10. scraper_chapter -> tracker_bookmark (0..1:N) -->
        <mxCell id="rel_c_bm" value="0..1 : N" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERzeroToOne;startFill=0;endArrow=ERzeroToMany;endFill=0;strokeWidth=2;strokeColor=#9333ea;fontStyle=1;labelBackgroundColor=#ffffff;" edge="1" parent="1" source="t_chapter" target="t_bookmark">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1350" y="440" />
              <mxPoint x="1145" y="480" />
              <mxPoint x="750" y="520" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Info & Legend Box -->
        <mxCell id="legend_box" value="&lt;b style='font-size: 13px;'&gt;CARDINALITY &amp;amp; NOTATION GUIDE&lt;/b&gt;&lt;hr&gt;&lt;div style='text-align: left; font-size: 11px; line-height: 1.6;'&gt;&lt;b&gt;PK&lt;/b&gt;: Primary Key &amp;nbsp;|&amp;nbsp; &lt;b&gt;FK&lt;/b&gt;: Foreign Key &amp;nbsp;|&amp;nbsp; &lt;b&gt;UQ&lt;/b&gt;: Unique Constraint &amp;nbsp;|&amp;nbsp; &lt;b&gt;NN&lt;/b&gt;: NOT NULL &amp;nbsp;|&amp;nbsp; &lt;b&gt;DF&lt;/b&gt;: Default Value&lt;br&gt;&lt;b&gt;Crow's Foot Notation:&lt;/b&gt; &lt;b&gt;—||—&lt;/b&gt; Mandatory One (1) &amp;nbsp;|&amp;nbsp; &lt;b&gt;—&amp;lt;&lt;/b&gt; Mandatory Many (N) &amp;nbsp;|&amp;nbsp; &lt;b&gt;—o&amp;lt;&lt;/b&gt; Zero or Many (0..N) &amp;nbsp;|&amp;nbsp; &lt;b&gt;—o|—&lt;/b&gt; Zero or One (0..1)&lt;br&gt;&lt;b&gt;Engine:&lt;/b&gt; PostgreSQL 17 Hosted on Supabase &amp;nbsp;|&amp;nbsp; &lt;b&gt;Architecture:&lt;/b&gt; Vertical Slice Architecture (Django 5.2)&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#cbd5e1;strokeWidth=1.5;arcSize=6;shadow=1;align=center;verticalAlign=top;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="390" y="660" width="1130" height="96" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
"""

with open(DRAWIO_PATH, "w", encoding="utf-8") as f:
    f.write(drawio_content.strip())
print(f"Created {DRAWIO_PATH}")

# 2. BEAUTIFUL PRINTABLE HTML WITH SVG CONNECTORS & CROW'S FOOT NOTATION
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Physical ERD - Royal Road Scraper</title>
<style>
  @page {
    size: A3 landscape;
    margin: 8mm;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
  }
  body {
    background-color: #f8fafc;
    color: #0f172a;
    padding: 10px;
    font-size: 11px;
    width: 1560px;
    position: relative;
  }
  .header {
    background: #ffffff;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    padding: 12px 20px;
    margin-bottom: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  .header h1 {
    font-size: 19px;
    font-weight: 700;
    color: #0f172a;
    letter-spacing: -0.3px;
  }
  .header .meta {
    font-size: 12px;
    color: #475569;
    margin-top: 3px;
  }
  .header .badge {
    background: #0f172a;
    color: #ffffff;
    padding: 6px 14px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 12px;
    letter-spacing: 0.5px;
  }

  /* Canvas Layout */
  .canvas {
    position: relative;
    width: 1540px;
    height: 820px;
    background: #f8fafc;
  }

  /* Table Box */
  .table-card {
    position: absolute;
    background: #ffffff;
    border: 1.5px solid #0f172a;
    border-radius: 7px;
    overflow: hidden;
    box-shadow: 0 3px 6px rgba(0,0,0,0.06);
    z-index: 10;
  }
  .table-header {
    background: #0f172a;
    color: #ffffff;
    padding: 6px 10px;
    font-weight: 700;
    font-size: 12.5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .table-header span.tag {
    font-size: 8.5px;
    background: #334155;
    color: #cbd5e1;
    padding: 2px 5px;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .table-rows {
    width: 100%;
    border-collapse: collapse;
  }
  .table-rows tr {
    border-bottom: 1px solid #f1f5f9;
  }
  .table-rows tr:last-child {
    border-bottom: none;
  }
  .table-rows td {
    padding: 4.5px 7px;
    font-size: 10.5px;
    line-height: 1.25;
  }
  .col-key {
    width: 32px;
    font-weight: 700;
    text-align: center;
  }
  .pk {
    color: #b91c1c;
    background-color: #fee2e2;
    border-radius: 3px;
    padding: 1px 3px;
    font-size: 9px;
    font-weight: bold;
  }
  .fk {
    color: #1d4ed8;
    background-color: #dbeafe;
    border-radius: 3px;
    padding: 1px 3px;
    font-size: 9px;
    font-weight: bold;
  }
  .uq {
    color: #047857;
    background-color: #d1fae5;
    border-radius: 3px;
    padding: 1px 3px;
    font-size: 8.5px;
    font-weight: bold;
  }
  .col-name {
    font-weight: 600;
    color: #1e293b;
  }
  .col-type {
    color: #64748b;
    font-family: 'Consolas', monospace;
    font-size: 10px;
    text-align: right;
  }

  /* SVG Relational Overlay */
  svg.rel-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 5;
    pointer-events: none;
  }
  .rel-line {
    fill: none;
    stroke-width: 2px;
  }
  .label-bg {
    fill: #ffffff;
    stroke-width: 1;
  }
  .card-label {
    font-size: 10px;
    font-weight: bold;
    text-anchor: middle;
    dominant-baseline: central;
  }

  /* Bottom Legend Box */
  .legend-bar {
    position: absolute;
    left: 360px;
    top: 670px;
    width: 1140px;
    background: #ffffff;
    border: 1.5px solid #cbd5e1;
    border-radius: 7px;
    padding: 10px 16px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    z-index: 10;
  }
  .legend-title {
    font-size: 11.5px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
  }
  .legend-items {
    display: flex;
    justify-content: space-between;
    font-size: 10.5px;
    color: #334155;
    line-height: 1.4;
  }
  .legend-item strong {
    color: #0f172a;
  }
</style>
</head>
<body>

<div class="header">
  <div>
    <h1>PHYSICAL ENTITY-RELATIONSHIP DIAGRAM (ERD)</h1>
    <div class="meta">
      <strong>Proposed System:</strong> Royal Road Scraper (<code>rrscraper</code>) &nbsp;|&nbsp;
      <strong>Database Engine:</strong> PostgreSQL 17 (Supabase) &nbsp;|&nbsp;
      <strong>Course:</strong> CSIT327 &nbsp;|&nbsp;
      <strong>Student:</strong> Yoji Macadangdang
    </div>
  </div>
  <div>
    <span class="badge">PHYSICAL DATA MODEL</span>
  </div>
</div>

<div class="canvas">

  <!-- SVG LINES & CROW'S FOOT CONNECTORS -->
  <svg class="rel-overlay">
    <defs>
      <!-- Crow's Foot Many Marker -->
      <marker id="crowsfoot-blue" viewBox="0 0 14 14" refX="12" refY="7" markerWidth="10" markerHeight="10" orient="auto">
        <path d="M 0 0 L 12 7 L 0 14 M 12 0 L 12 14" stroke="#1d4ed8" stroke-width="1.8" fill="none" />
      </marker>
      <marker id="crowsfoot-green" viewBox="0 0 14 14" refX="12" refY="7" markerWidth="10" markerHeight="10" orient="auto">
        <path d="M 0 0 L 12 7 L 0 14 M 12 0 L 12 14" stroke="#059669" stroke-width="1.8" fill="none" />
      </marker>
      <marker id="crowsfoot-amber" viewBox="0 0 14 14" refX="12" refY="7" markerWidth="10" markerHeight="10" orient="auto">
        <path d="M 0 0 L 12 7 L 0 14 M 12 0 L 12 14" stroke="#d97706" stroke-width="1.8" fill="none" />
      </marker>
      <marker id="crowsfoot-red" viewBox="0 0 14 14" refX="12" refY="7" markerWidth="10" markerHeight="10" orient="auto">
        <path d="M 0 0 L 12 7 L 0 14 M 12 0 L 12 14" stroke="#dc2626" stroke-width="1.8" fill="none" />
      </marker>
      <marker id="crowsfoot-purple" viewBox="0 0 14 14" refX="12" refY="7" markerWidth="10" markerHeight="10" orient="auto">
        <path d="M 0 0 L 12 7 L 0 14 M 12 0 L 12 14" stroke="#9333ea" stroke-width="1.8" fill="none" />
      </marker>
      <marker id="crowsfoot-teal" viewBox="0 0 14 14" refX="12" refY="7" markerWidth="10" markerHeight="10" orient="auto">
        <path d="M 0 0 L 12 7 L 0 14 M 12 0 L 12 14" stroke="#0891b2" stroke-width="1.8" fill="none" />
      </marker>

      <!-- Mandatory One Marker (Double bar) -->
      <marker id="one-start" viewBox="0 0 12 12" refX="2" refY="6" markerWidth="8" markerHeight="8" orient="auto">
        <path d="M 3 1 L 3 11 M 7 1 L 7 11" stroke="#334155" stroke-width="1.8" fill="none" />
      </marker>
      <marker id="one-end" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="8" markerHeight="8" orient="auto">
        <path d="M 5 1 L 5 11 M 9 1 L 9 11" stroke="#334155" stroke-width="1.8" fill="none" />
      </marker>
      <!-- Optional One Marker (Circle + Bar) -->
      <marker id="zero-one-start" viewBox="0 0 16 12" refX="2" refY="6" markerWidth="10" markerHeight="8" orient="auto">
        <circle cx="5" cy="6" r="3.5" stroke="#9333ea" stroke-width="1.5" fill="none" />
        <path d="M 12 1 L 12 11" stroke="#9333ea" stroke-width="1.8" fill="none" />
      </marker>
    </defs>

    <!-- 1. auth_user -> profile_profile (1:1) -->
    <path d="M 155 376 L 155 430" stroke="#1d4ed8" class="rel-line" marker-start="url(#one-start)" marker-end="url(#one-end)" />
    <rect x="140" y="395" width="30" height="15" rx="3" class="label-bg" stroke="#1d4ed8" />
    <text x="155" y="402" class="card-label" fill="#1d4ed8">1 : 1</text>

    <!-- 2. profile_profile -> user_settings (1:1) -->
    <path d="M 155 575 L 155 625" stroke="#1d4ed8" class="rel-line" marker-start="url(#one-start)" marker-end="url(#one-end)" />
    <rect x="140" y="592" width="30" height="15" rx="3" class="label-bg" stroke="#1d4ed8" />
    <text x="155" y="599" class="card-label" fill="#1d4ed8">1 : 1</text>

    <!-- 3. auth_user -> scraper_job (1:N) -->
    <path d="M 290 190 L 360 190" stroke="#059669" class="rel-line" marker-start="url(#one-start)" marker-end="url(#crowsfoot-green)" />
    <rect x="312" y="182" width="28" height="15" rx="3" class="label-bg" stroke="#059669" />
    <text x="326" y="189" class="card-label" fill="#059669">1:N</text>

    <!-- 4. auth_user -> tracker_bookmark (1:N) -->
    <path d="M 290 320 L 325 320 L 325 450 L 360 450" stroke="#059669" class="rel-line" marker-start="url(#one-start)" marker-end="url(#crowsfoot-green)" />
    <rect x="310" y="375" width="28" height="15" rx="3" class="label-bg" stroke="#059669" />
    <text x="324" y="382" class="card-label" fill="#059669">1:N</text>

    <!-- 5. scraper_novel -> scraper_job (1:0..N) -->
    <path d="M 740 210 L 670 210" stroke="#d97706" class="rel-line" marker-start="url(#one-start)" marker-end="url(#crowsfoot-amber)" />
    <rect x="690" y="202" width="30" height="15" rx="3" class="label-bg" stroke="#d97706" />
    <text x="705" y="209" class="card-label" fill="#d97706">1:0..N</text>

    <!-- 6. scraper_novel -> tracker_bookmark (1:N) -->
    <path d="M 740 370 L 705 370 L 705 470 L 670 470" stroke="#d97706" class="rel-line" marker-start="url(#one-start)" marker-end="url(#crowsfoot-amber)" />
    <rect x="690" y="410" width="28" height="15" rx="3" class="label-bg" stroke="#d97706" />
    <text x="704" y="417" class="card-label" fill="#d97706">1:N</text>

    <!-- 7. scraper_novel -> scraper_chapter (1:N) -->
    <path d="M 1070 240 L 1140 240" stroke="#dc2626" class="rel-line" marker-start="url(#one-start)" marker-end="url(#crowsfoot-red)" />
    <rect x="1092" y="232" width="28" height="15" rx="3" class="label-bg" stroke="#dc2626" />
    <text x="1106" y="239" class="card-label" fill="#dc2626">1:N</text>

    <!-- 8. scraper_novel -> scraper_novel_tags (1:N) -->
    <path d="M 905 460 L 905 520" stroke="#0891b2" class="rel-line" marker-start="url(#one-start)" marker-end="url(#crowsfoot-teal)" />
    <rect x="890" y="483" width="28" height="15" rx="3" class="label-bg" stroke="#0891b2" />
    <text x="904" y="490" class="card-label" fill="#0891b2">1:N</text>

    <!-- 9. scraper_tag -> scraper_novel_tags (1:N) -->
    <path d="M 1140 575 L 1070 575" stroke="#0891b2" class="rel-line" marker-start="url(#one-start)" marker-end="url(#crowsfoot-teal)" />
    <rect x="1092" y="567" width="28" height="15" rx="3" class="label-bg" stroke="#0891b2" />
    <text x="1106" y="574" class="card-label" fill="#0891b2">1:N</text>

    <!-- 10. scraper_chapter -> tracker_bookmark (0..1:N) -->
    <path d="M 1200 410 L 1200 490 L 670 490" stroke="#9333ea" class="rel-line" marker-start="url(#zero-one-start)" marker-end="url(#crowsfoot-purple)" />
    <rect x="980" y="482" width="40" height="15" rx="3" class="label-bg" stroke="#9333ea" />
    <text x="1000" y="489" class="card-label" fill="#9333ea">0..1 : N</text>
  </svg>

  <!-- TABLE: auth_user (x=20, y=100, w=270, h=276) -->
  <div class="table-card" style="left: 20px; top: 100px; width: 270px;">
    <div class="table-header">
      auth_user
      <span class="tag">Auth Core</span>
    </div>
    <table class="table-rows">
      <tr><td class="col-key"><span class="pk">PK</span></td><td class="col-name">id</td><td class="col-type">INTEGER</td></tr>
      <tr><td class="col-key"><span class="uq">UQ</span></td><td class="col-name">username</td><td class="col-type">VARCHAR(150)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">email</td><td class="col-type">VARCHAR(254)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">password</td><td class="col-type">VARCHAR(128)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">first_name</td><td class="col-type">VARCHAR(150)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">last_name</td><td class="col-type">VARCHAR(150)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">is_active</td><td class="col-type">BOOLEAN</td></tr>
      <tr><td class="col-key"></td><td class="col-name">is_staff</td><td class="col-type">BOOLEAN</td></tr>
      <tr><td class="col-key"></td><td class="col-name">is_superuser</td><td class="col-type">BOOLEAN</td></tr>
      <tr><td class="col-key"></td><td class="col-name">date_joined</td><td class="col-type">TIMESTAMPTZ</td></tr>
      <tr><td class="col-key"></td><td class="col-name">last_login</td><td class="col-type">TIMESTAMPTZ</td></tr>
    </table>
  </div>

  <!-- TABLE: profile_profile (x=20, y=430, w=270, h=145) -->
  <div class="table-card" style="left: 20px; top: 430px; width: 270px;">
    <div class="table-header">
      profile_profile
      <span class="tag">Profile Slice</span>
    </div>
    <table class="table-rows">
      <tr><td class="col-key"><span class="pk">PK</span></td><td class="col-name">id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"><span class="fk">FK</span></td><td class="col-name">user_id <span class="uq">UQ</span></td><td class="col-type">INTEGER</td></tr>
      <tr><td class="col-key"></td><td class="col-name">full_name</td><td class="col-type">VARCHAR(150)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">bio</td><td class="col-type">TEXT</td></tr>
      <tr><td class="col-key"></td><td class="col-name">profile_image</td><td class="col-type">VARCHAR(100)</td></tr>
    </table>
  </div>

  <!-- TABLE: user_settings_usersettings (x=20, y=625, w=270, h=120) -->
  <div class="table-card" style="left: 20px; top: 625px; width: 270px;">
    <div class="table-header">
      user_settings_usersettings
      <span class="tag">Settings Slice</span>
    </div>
    <table class="table-rows">
      <tr><td class="col-key"><span class="pk">PK</span></td><td class="col-name">id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"><span class="fk">FK</span></td><td class="col-name">user_id <span class="uq">UQ</span></td><td class="col-type">INTEGER</td></tr>
      <tr><td class="col-key"></td><td class="col-name">dark_mode</td><td class="col-type">BOOLEAN</td></tr>
      <tr><td class="col-key"></td><td class="col-name">email_notifications</td><td class="col-type">BOOLEAN</td></tr>
    </table>
  </div>

  <!-- TABLE: scraper_job (x=360, y=100, w=310, h=240) -->
  <div class="table-card" style="left: 360px; top: 100px; width: 310px;">
    <div class="table-header">
      scraper_job
      <span class="tag">Scraper Task</span>
    </div>
    <table class="table-rows">
      <tr><td class="col-key"><span class="pk">PK</span></td><td class="col-name">id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"><span class="fk">FK</span></td><td class="col-name">user_id</td><td class="col-type">INTEGER</td></tr>
      <tr><td class="col-key"><span class="fk">FK</span></td><td class="col-name">novel_id (NULL)</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"></td><td class="col-name">target_url</td><td class="col-type">VARCHAR(500)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">status</td><td class="col-type">VARCHAR(30)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">chapters_scraped</td><td class="col-type">INTEGER</td></tr>
      <tr><td class="col-key"></td><td class="col-name">error_message</td><td class="col-type">TEXT</td></tr>
      <tr><td class="col-key"></td><td class="col-name">started_at</td><td class="col-type">TIMESTAMPTZ</td></tr>
      <tr><td class="col-key"></td><td class="col-name">completed_at</td><td class="col-type">TIMESTAMPTZ</td></tr>
    </table>
  </div>

  <!-- TABLE: tracker_bookmark (x=360, y=380, w=310, h=245) -->
  <div class="table-card" style="left: 360px; top: 380px; width: 310px;">
    <div class="table-header">
      tracker_bookmark
      <span class="tag">User Library</span>
    </div>
    <table class="table-rows">
      <tr><td class="col-key"><span class="pk">PK</span></td><td class="col-name">id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"><span class="fk">FK</span></td><td class="col-name">user_id</td><td class="col-type">INTEGER</td></tr>
      <tr><td class="col-key"><span class="fk">FK</span></td><td class="col-name">novel_id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"><span class="fk">FK</span></td><td class="col-name">last_read_chapter_id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"></td><td class="col-name">reading_status</td><td class="col-type">VARCHAR(30)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">is_favorite</td><td class="col-type">BOOLEAN</td></tr>
      <tr><td class="col-key"></td><td class="col-name">last_read_at</td><td class="col-type">TIMESTAMPTZ</td></tr>
      <tr><td class="col-key"></td><td class="col-name">created_at</td><td class="col-type">TIMESTAMPTZ</td></tr>
      <tr><td colspan="3" style="font-size: 8.5px; color: #64748b; font-style: italic; text-align: center; background: #f8fafc;">UQ(user_id, novel_id)</td></tr>
    </table>
  </div>

  <!-- TABLE: scraper_novel (x=740, y=140, w=330, h=320) -->
  <div class="table-card" style="left: 740px; top: 140px; width: 330px;">
    <div class="table-header">
      scraper_novel
      <span class="tag">Fiction Core</span>
    </div>
    <table class="table-rows">
      <tr><td class="col-key"><span class="pk">PK</span></td><td class="col-name">id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"><span class="uq">UQ</span></td><td class="col-name">royalroad_id</td><td class="col-type">VARCHAR(50)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">title</td><td class="col-type">VARCHAR(255)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">author_name</td><td class="col-type">VARCHAR(150)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">synopsis</td><td class="col-type">TEXT</td></tr>
      <tr><td class="col-key"></td><td class="col-name">cover_image_url</td><td class="col-type">VARCHAR(500)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">status</td><td class="col-type">VARCHAR(30)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">rating</td><td class="col-type">NUMERIC(3,2)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">total_pages</td><td class="col-type">INTEGER</td></tr>
      <tr><td class="col-key"></td><td class="col-name">source_url</td><td class="col-type">VARCHAR(500)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">created_at</td><td class="col-type">TIMESTAMPTZ</td></tr>
      <tr><td class="col-key"></td><td class="col-name">updated_at</td><td class="col-type">TIMESTAMPTZ</td></tr>
    </table>
  </div>

  <!-- TABLE: scraper_novel_tags (x=740, y=520, w=330, h=115) -->
  <div class="table-card" style="left: 740px; top: 520px; width: 330px;">
    <div class="table-header">
      scraper_novel_tags
      <span class="tag">Junction (M:N)</span>
    </div>
    <table class="table-rows">
      <tr><td class="col-key"><span class="pk">PK</span></td><td class="col-name">id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"><span class="fk">FK</span></td><td class="col-name">novel_id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"><span class="fk">FK</span></td><td class="col-name">tag_id</td><td class="col-type">BIGINT</td></tr>
      <tr><td colspan="3" style="font-size: 8.5px; color: #64748b; font-style: italic; text-align: center; background: #f8fafc;">UQ(novel_id, tag_id)</td></tr>
    </table>
  </div>

  <!-- TABLE: scraper_chapter (x=1140, y=140, w=330, h=270) -->
  <div class="table-card" style="left: 1140px; top: 140px; width: 330px;">
    <div class="table-header">
      scraper_chapter
      <span class="tag">Chapter Content</span>
    </div>
    <table class="table-rows">
      <tr><td class="col-key"><span class="pk">PK</span></td><td class="col-name">id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"><span class="fk">FK</span></td><td class="col-name">novel_id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"></td><td class="col-name">royalroad_chapter_id</td><td class="col-type">VARCHAR(50)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">chapter_number</td><td class="col-type">INTEGER</td></tr>
      <tr><td class="col-key"></td><td class="col-name">title</td><td class="col-type">VARCHAR(255)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">content</td><td class="col-type">TEXT</td></tr>
      <tr><td class="col-key"></td><td class="col-name">word_count</td><td class="col-type">INTEGER</td></tr>
      <tr><td class="col-key"></td><td class="col-name">source_url</td><td class="col-type">VARCHAR(500)</td></tr>
      <tr><td class="col-key"></td><td class="col-name">release_date</td><td class="col-type">TIMESTAMPTZ</td></tr>
      <tr><td class="col-key"></td><td class="col-name">scraped_at</td><td class="col-type">TIMESTAMPTZ</td></tr>
    </table>
  </div>

  <!-- TABLE: scraper_tag (x=1140, y=520, w=330, h=105) -->
  <div class="table-card" style="left: 1140px; top: 520px; width: 330px;">
    <div class="table-header">
      scraper_tag
      <span class="tag">Genres &amp; Tags</span>
    </div>
    <table class="table-rows">
      <tr><td class="col-key"><span class="pk">PK</span></td><td class="col-name">id</td><td class="col-type">BIGINT</td></tr>
      <tr><td class="col-key"><span class="uq">UQ</span></td><td class="col-name">name</td><td class="col-type">VARCHAR(50)</td></tr>
      <tr><td class="col-key"><span class="uq">UQ</span></td><td class="col-name">slug</td><td class="col-type">VARCHAR(50)</td></tr>
    </table>
  </div>

  <!-- LEGEND & CARDINALITY BAR -->
  <div class="legend-bar">
    <div class="legend-title">
      <span>DIAGRAM LEGEND &amp; CARDINALITY NOTATION</span>
      <span style="font-weight: normal; font-size: 10px; color: #64748b;">PostgreSQL 17 | Supabase Hosted | Django 5.2</span>
    </div>
    <div class="legend-items">
      <div class="legend-item">
        <strong>Field Keys:</strong><br>
        <span class="pk">PK</span> Primary Key<br>
        <span class="fk">FK</span> Foreign Key<br>
        <span class="uq">UQ</span> Unique Field
      </div>
      <div class="legend-item">
        <strong>Crow's Foot Notation:</strong><br>
        <strong>—||—</strong> Mandatory One (1)<br>
        <strong>—&lt;</strong> Mandatory Many (N)<br>
        <strong>—o&lt;</strong> Zero or Many (0..N)<br>
        <strong>—o|—</strong> Zero or One (0..1)
      </div>
      <div class="legend-item">
        <strong>Primary Relationships:</strong><br>
        • <code>auth_user</code> (1) ↔ (1) <code>profile_profile</code> / <code>user_settings</code><br>
        • <code>auth_user</code> (1) ↔ (N) <code>scraper_job</code> / <code>tracker_bookmark</code><br>
        • <code>scraper_novel</code> (1) ↔ (N) <code>scraper_chapter</code>
      </div>
      <div class="legend-item">
        <strong>Domain Logic:</strong><br>
        • <code>scraper_novel</code> (1) ↔ (0..N) <code>scraper_job</code><br>
        • <code>scraper_novel</code> (M) ↔ (N) <code>scraper_tag</code> (via <code>novel_tags</code>)<br>
        • <code>tracker_bookmark</code> (N) ↔ (0..1) <code>scraper_chapter</code>
      </div>
    </div>
  </div>

</div>

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content.strip())
print(f"Created {HTML_PATH}")

# 3. RE-GENERATE PDF AND SCREENSHOT
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
print("Generating PDF via Chrome...")
subprocess.run([
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--print-to-pdf={PDF_PATH}",
    str(HTML_PATH)
], capture_output=True, text=True)

print("Generating Screenshot via Chrome...")
subprocess.run([
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    f"--screenshot={BASE_DIR / 'erd_screenshot.png'}",
    "--window-size=1600,950",
    str(HTML_PATH)
], capture_output=True, text=True)

if PDF_PATH.exists():
    print(f"Success! PDF size: {PDF_PATH.stat().st_size} bytes")
