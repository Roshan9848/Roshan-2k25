<!DOCTYPE html>
<!-- saved from url=(0034)https://colab.research.google.com/ -->
<html lang="en" editor="Default Dark" theme="dark"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script type="text/javascript" async="" charset="utf-8" src="./python_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-8mJgBUBw4uTWF9Ooxgb4sUuO9jKtaVm1I+8vb0qpxxX3cafec7ovH+goM3yD4UyO" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./python_files/recaptcha__en.js.download" crossorigin="anonymous" integrity="sha384-8mJgBUBw4uTWF9Ooxgb4sUuO9jKtaVm1I+8vb0qpxxX3cafec7ovH+goM3yD4UyO" nonce=""></script><script src="./python_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./python_files/cb=gapi.loaded_0" nonce="" async=""></script><script type="text/javascript" async="" src="./python_files/js" nonce=""></script><script async="" src="./python_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Welcome To Colab - Colab</title><link href="./python_files/css2" rel="stylesheet"><link href="./python_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_2d:not(.gb_pe){font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Pa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_Pa:hover::after,a.gb_Pa:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Pa:hover,a.gb_Pa:focus{text-decoration:none}a.gb_Pa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Qa{background-color:#4285f4;color:#fff}a.gb_Qa:active{background-color:#0043b2}.gb_Ra{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Pa,.gb_Qa,.gb_Sa,.gb_Ta{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Sa{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ta{background:#f8f8f8}.gb_Sa,#gb a.gb_Sa.gb_Sa,.gb_Ta{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ta{cursor:default;text-decoration:none}.gb_Ta{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ta{color:#fff}.gb_Ta:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ta:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Ua{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Ua:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Ua:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Ua:active,#gb .gb_Ua:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Ua.gb_F{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Ua.gb_F:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Ua.gb_F:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Ua.gb_F:active,#gb .gb_Ua.gb_F:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_bd{display:inline-block;vertical-align:middle}.gb_Oe .gb_P{bottom:-3px;right:-5px}.gb_C{position:relative}.gb_A{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_A{cursor:pointer;text-decoration:none}.gb_A,a.gb_A{color:#000}.gb_cd{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_dd{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_dd{border-bottom-color:#ccc}.gb_ka{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_bd.gb_Sc .gb_cd,.gb_bd.gb_Sc .gb_dd,.gb_bd.gb_Sc .gb_ka,.gb_Sc.gb_ka{display:block}.gb_bd.gb_Sc.gb_ed .gb_cd,.gb_bd.gb_Sc.gb_ed .gb_dd{display:none}.gb_Pe{position:absolute;right:8px;top:62px;z-index:-1}.gb_fd .gb_cd,.gb_fd .gb_dd,.gb_fd .gb_ka{margin-top:-10px}.gb_bd:first-child,#gbsfw:first-child+.gb_bd{padding-left:4px}.gb_Ea.gb_Qe .gb_bd:first-child{padding-left:0}.gb_Re{position:relative}.gb_1c .gb_Re,.gb_Id .gb_Re{float:right}.gb_A{padding:8px;cursor:pointer}.gb_A::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Ea .gb_gd:not(.gb_Pa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_hd button svg,.gb_A{-webkit-border-radius:50%;border-radius:50%}.gb_hd button:focus:not(:focus-visible) svg,.gb_hd button:hover svg,.gb_hd button:active svg,.gb_A:focus:not(:focus-visible),.gb_A:hover,.gb_A:active,.gb_A[aria-expanded=true]{outline:none}.gb_Kc .gb_hd.gb_id button:focus-visible svg,.gb_hd button:focus-visible svg,.gb_A:focus-visible{outline:1px solid #202124}.gb_Kc .gb_hd button:focus-visible svg,.gb_Kc .gb_A:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Kc .gb_hd.gb_id button:focus-visible svg,.gb_hd button:focus-visible svg,.gb_Kc .gb_hd button:focus-visible svg{outline:1px solid currentcolor}}.gb_Kc .gb_hd.gb_id button:focus svg,.gb_Kc .gb_hd.gb_id button:focus:hover svg,.gb_hd button:focus svg,.gb_hd button:focus:hover svg,.gb_A:focus,.gb_A:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Kc .gb_hd.gb_id button:active svg,.gb_hd button:active svg,.gb_A:active{background-color:rgba(60,64,67,.12)}.gb_Kc .gb_hd.gb_id button:hover svg,.gb_hd button:hover svg,.gb_A:hover{background-color:rgba(60,64,67,.08)}.gb_Va .gb_A.gb_Xa:hover{background-color:transparent}.gb_A[aria-expanded=true],.gb_A:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_A[aria-expanded=true] .gb_E{fill:#5f6368;opacity:1}.gb_Kc .gb_hd button:hover svg,.gb_Kc .gb_A:hover{background-color:rgba(232,234,237,.08)}.gb_Kc .gb_hd button:focus svg,.gb_Kc .gb_hd button:focus:hover svg,.gb_Kc .gb_A:focus,.gb_Kc .gb_A:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Kc .gb_hd button:active svg,.gb_Kc .gb_A:active{background-color:rgba(232,234,237,.12)}.gb_Kc .gb_A[aria-expanded=true],.gb_Kc .gb_A:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Kc .gb_A[aria-expanded=true] .gb_E{fill:#fff;opacity:1}.gb_bd{padding:4px}.gb_Ea.gb_Qe .gb_bd{padding:4px 2px}.gb_Ea.gb_Qe .gb_y.gb_bd{padding-left:6px}.gb_ka{z-index:991;line-height:normal}.gb_ka.gb_jd{left:0;right:auto}@media (max-width:350px){.gb_ka.gb_jd{left:0}}.gb_Se .gb_ka{top:56px}.gb_Q{display:none!important}.gb_md{visibility:hidden}.gb_I .gb_A,.gb_ja .gb_I .gb_A{background-position:-64px -29px}.gb_0 .gb_I .gb_A{background-position:-29px -29px;opacity:1}.gb_I .gb_A,.gb_I .gb_A:hover,.gb_I .gb_A:focus{opacity:1}.gb_K{display:none}@media screen and (max-width:319px){.gb_kd:not(.gb_ld) .gb_I{display:none;visibility:hidden}}.gb_P{display:none}.gb_8c{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_8c.gb_9c{color:#3c4043}.gb_Ea.gb_bc .gb_8c{margin-bottom:0}.gb_rd.gb_td .gb_8c{padding-left:4px}.gb_Ea.gb_bc .gb_ud{position:relative;top:-2px}.gb_ad{display:none}.gb_Ea{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Ea.gb_Rc{min-width:120px}.gb_Ea.gb_vd .gb_wd{display:none}.gb_Ea.gb_vd .gb_kd{height:56px}header.gb_Ea{display:block}.gb_Ea svg{fill:currentColor}.gb_Cd{position:fixed;top:0;width:100%}.gb_xd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Dd{height:64px}.gb_kd{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Ea:not(.gb_bc) .gb_kd{padding:8px}.gb_Ea.gb_Ed .gb_kd{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Ea .gb_kd.gb_ld.gb_Fd{min-width:0}.gb_Ea.gb_bc .gb_kd{padding:4px;padding-left:8px;min-width:0}.gb_wd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_zd>.gb_wd{display:table-cell;width:100%}.gb_rd{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Ea.gb_bc .gb_rd{padding-right:14px}.gb_Ad{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Ad>:only-child{display:inline-block}.gb_Bd.gb_2c{padding-left:4px}.gb_Bd.gb_Hd,.gb_Ea.gb_Ed .gb_Bd,.gb_Ea.gb_bc:not(.gb_Id) .gb_Bd{padding-left:0}.gb_Ea.gb_bc .gb_Bd.gb_Hd{padding-right:0}.gb_Ea.gb_bc .gb_Bd.gb_Hd .gb_Va{margin-left:10px}.gb_2c{display:inline}.gb_Ea.gb_Vc .gb_Bd.gb_Jd,.gb_Ea.gb_Id .gb_Bd.gb_Jd{padding-left:2px}.gb_8c{display:inline-block}.gb_Bd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Id{height:48px}.gb_Ea.gb_Id{min-width:auto}.gb_Id .gb_Bd{float:right;padding-left:32px}.gb_Id .gb_Bd.gb_Kd{padding-left:0}.gb_Ld{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_od{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Md{color:black}.gb_Kc{color:white}.gb_Ea a,.gb_Oc a{color:inherit}.gb_aa{color:rgba(0,0,0,.87)}.gb_Ea svg,.gb_Oc svg,.gb_rd .gb_sd,.gb_1c .gb_sd{color:#5f6368;opacity:1}.gb_Kc svg,.gb_Oc.gb_Tc svg,.gb_Kc .gb_rd .gb_sd,.gb_Kc .gb_rd .gb_Jc,.gb_Kc .gb_rd .gb_ud,.gb_Oc.gb_Tc .gb_sd{color:rgba(255,255,255,.87)}.gb_Kc .gb_rd .gb_Nd:not(.gb_Od){opacity:.87}.gb_9c{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Kc .gb_9c,.gb_Md .gb_9c{opacity:1}.gb_Pd{position:relative}.gb_L{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_W,span.gb_W{color:rgba(0,0,0,.87);text-decoration:none}.gb_Kc a.gb_W,.gb_Kc span.gb_W{color:white}a.gb_W:focus{outline-offset:2px}a.gb_W:hover{text-decoration:underline}.gb_X{display:inline-block;padding-left:15px}.gb_X .gb_W{display:inline-block;line-height:24px;vertical-align:middle}.gb_pd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Ea.gb_Id .gb_pd{margin-left:8px}#gb a.gb_Ta.gb_pd{cursor:pointer}.gb_Ta.gb_pd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ta.gb_pd:focus,.gb_Ta.gb_pd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ta.gb_pd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_pd{background:#1a73e8;border:1px solid transparent}.gb_Ea.gb_bc .gb_pd{padding:9px 15px;min-width:80px}.gb_Qd{text-align:left}#gb .gb_Kc a.gb_pd:not(.gb_F),#gb.gb_Kc a.gb_pd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ta.gb_F.gb_pd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Kc a.gb_pd:hover:not(.gb_F),#gb.gb_Kc a.gb_pd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ta.gb_F.gb_pd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Kc a.gb_pd:focus:not(.gb_F),#gb .gb_Kc a.gb_pd:focus:hover:not(.gb_F),#gb.gb_Kc a.gb_pd:focus:not(.gb_F),#gb.gb_Kc a.gb_pd:focus:hover:not(.gb_F){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ta.gb_F.gb_pd:focus,#gb a.gb_Ta.gb_F.gb_pd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Kc a.gb_pd:active:not(.gb_F),#gb.gb_Kc a.gb_pd:active{background:#ecf3fe}#gb a.gb_Ta.gb_F.gb_pd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_J{display:none}@media screen and (max-width:319px){.gb_kd .gb_I{display:none;visibility:hidden}}.gb_Va{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Va.gb_F{background-color:transparent;border:1px solid #5f6368}.gb_2a{display:inherit}.gb_Va.gb_F .gb_2a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Va:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Va.gb_F:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Va:focus-visible,.gb_Va:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Va.gb_F:focus-visible,.gb_Va.gb_F:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Va.gb_F:active,.gb_Va.gb_Sc.gb_F:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_3a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Va.gb_F .gb_3a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_3a.gb_4a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_3a.gb_4a .gb_Hc{vertical-align:middle}.gb_Ea:not(.gb_bc) .gb_Va{margin-left:10px;margin-right:4px}.gb_Rd{max-height:32px;width:78px}.gb_Va.gb_F .gb_Rd{max-height:26px;width:72px}.gb_O{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_db{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_db.gb_O{height:30px;width:30px}.gb_db.gb_O:hover,.gb_db.gb_O:active{-webkit-box-shadow:none;box-shadow:none}.gb_eb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_vc{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_O::before,.gb_fb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_2 .gb_fb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_O:hover,.gb_O:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_O:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_O:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_gb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_A.gb_gb{width:auto}.gb_gb:hover,.gb_gb:focus{opacity:.85}.gb_fd .gb_gb,.gb_fd .gb_Ud{line-height:26px}#gb#gb.gb_fd a.gb_gb,.gb_fd .gb_Ud{font-size:11px;height:auto}.gb_hb{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Xa:hover .gb_hb{opacity:.85}.gb_Va>.gb_y{padding:3px 3px 3px 4px}.gb_Vd.gb_md{color:#fff}.gb_0 .gb_gb,.gb_0 .gb_hb{opacity:1}#gb#gb.gb_0.gb_0 a.gb_gb,#gb#gb .gb_0.gb_0 a.gb_gb{color:#fff}.gb_0.gb_0 .gb_hb{border-top-color:#fff;opacity:1}.gb_ja .gb_O:hover,.gb_0 .gb_O:hover,.gb_ja .gb_O:focus,.gb_0 .gb_O:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_Wd .gb_y,.gb_Xd .gb_y{position:absolute;right:1px}.gb_y.gb_Z,.gb_ib.gb_Z,.gb_Xa.gb_Z{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_Zd.gb_0d .gb_gb{width:30px!important}.gb_1d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_2d .gb_1d,.gb_3d .gb_1d{right:0;top:0}.gb_y .gb_A{padding:4px}.gb_R{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.otmEBJ358uU.2019.O","co.in","en","425",0,[4,2,"","","","706535361","0"],null,"4oN7Z7LcCJfgp84P8JPaqA0",null,0,"og.qtm.zyyRgCCaN80.L.W.O","AA2YrTu0yU9RTMfNNC-LVUmaaNKwIO136g","AA2YrTs4SLbgh5FvGZPW_Ny7TyTdXfy6xA","",2,1,200,"IND",null,null,"425","425",1,null,null,114591953,1,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","sunnyrockzzmadani@gmail.com","","AJP8KkXlcv9k1S_sxxezQS0onXutv-DVZLE3fxSbMphHZNKOZpmeg453RTayWEY6uqtpVnDGU44goKnk-YUHT2Ut3kFBkoOMJw",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",0,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.ZpMpph_5a4M.O/d=1/rs=AHpOoo_c5__TAiALeuHoQOKG0BnSpdbJrQ/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20241202.0_p1","en",null,0],[0.009999999776482582,"co.in","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"IND","en","706535361.0",8,null,1,0,null,null,null,null,"3700949,102278209,102278211",null,null,null,"4oN7Z7LcCJfgp84P8JPaqA0",0,0,0,null,2,5,"nn",190,0,0,0,0,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.otmEBJ358uU.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTu0yU9RTMfNNC-LVUmaaNKwIO136g"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.zyyRgCCaN80.L.W.O/m=qcwid,qba/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTs4SLbgh5FvGZPW_Ny7TyTdXfy6xA"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?yac=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",1,1],0,1,null,1,1,1,1,null,null,0,0,0,null,0,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=en\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en\u0026continue=https://colab.research.google.com/\u0026timeStmp=1736147938\u0026secTok=.AG5fkS-iX2p9cyfAy3Cdk0eWr6LOCTlI-w\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",1,1,0,0,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,1,null,0,null,0],0,null,null,null,1],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ca,ja,ka,oa,qa,ra,Aa,Ba,Da,Ea,Fa,Ia,Va,Ua,Ya,$a,Za,ab,bb,eb,fb,jb,mb,gb,lb,kb,ib,hb,nb,pb,wb,Ab,Bb,Cb,Db;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.Hj=!0;return a};ca=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};
_.da=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ea=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};ja=function(a){return fa?ia?ia.brands.some(({brand:b})=>b&&b.indexOf(a)!=-1):!1:!1};_.u=function(a){return _.ea().indexOf(a)!=-1};ka=function(){return fa?!!ia&&ia.brands.length>0:!1};_.la=function(){return ka()?!1:_.u("Opera")};_.ma=function(){return ka()?!1:_.u("Trident")||_.u("MSIE")};_.na=function(){return _.u("Firefox")||_.u("FxiOS")};
_.pa=function(){return _.u("Safari")&&!(oa()||(ka()?0:_.u("Coast"))||_.la()||(ka()?0:_.u("Edge"))||(ka()?ja("Microsoft Edge"):_.u("Edg/"))||(ka()?ja("Opera"):_.u("OPR"))||_.na()||_.u("Silk")||_.u("Android"))};oa=function(){return ka()?ja("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(ka()?0:_.u("Edge"))||_.u("Silk")};qa=function(){return fa?!!ia&&!!ia.platform:!1};ra=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.sa=function(){return ra()||_.u("iPad")||_.u("iPod")};
_.ta=function(){return qa()?ia.platform==="macOS":_.u("Macintosh")};_.va=function(a,b){return _.ua(a,b)>=0};_.wa=function(a){let b="",c=0;const d=a.length-10240;for(;c<d;)b+=String.fromCharCode.apply(null,a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);return btoa(b)};_.xa=function(a){return a!=null&&a instanceof Uint8Array};_.ya=function(a){return Array.prototype.slice.call(a)};_.za=function(a){return!!((a[_.v]|0)&2)};Aa=function(a,b){b[_.v]=(a|0)&-30975};
Ba=function(a,b){b[_.v]=(a|34)&-30941};Da=function(a){return!(!a||typeof a!=="object"||a.i!==Ca)};Ea=function(a){return a!==null&&typeof a==="object"&&!Array.isArray(a)&&a.constructor===Object};Fa=function(a){return!Array.isArray(a)||a.length?!1:(a[_.v]|0)&1?!0:!1};_.Ga=function(a){if(a&2)throw Error();};Ia=function(a,b){(b=_.Ha?b[_.Ha]:void 0)&&(a[_.Ha]=_.ya(b))};_.Ka=function(){const a=Error();Ja(a,"incident");_.da(a)};_.La=function(a){a=Error(a);Ja(a,"warning");return a};
_.Na=function(a){if(typeof a!=="boolean")throw Error("s`"+_.Ma(a)+"`"+a);return a};_.Oa=function(a){if(!Number.isFinite(a))throw _.La("enum");return a|0};_.Pa=function(a){if(typeof a!=="number")throw _.La("int32");if(!Number.isFinite(a))throw _.La("int32");return a|0};_.Qa=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};_.Ra=function(a){return a==null||typeof a==="string"?a:void 0};
_.Ta=function(a,b,c){if(a!=null&&typeof a==="object"&&a.Fd===_.Sa)return a;if(Array.isArray(a)){var d=a[_.v]|0,e=d;e===0&&(e|=c&32);e|=c&2;e!==d&&(a[_.v]=e);return new b(a)}};Va=function(a,b){return Ua(b)};Ua=function(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "bigint":return(0,_.Wa)(a)?Number(a):String(a);case "boolean":return a?1:0;case "object":if(a)if(Array.isArray(a)){if(Fa(a))return}else{if(_.xa(a))return _.wa(a);if("function"==typeof _.Xa&&a instanceof _.Xa)return a.j()}}return a};
Ya=function(a,b,c){const d=_.ya(a);var e=d.length;const f=b&256?d[e-1]:void 0;e+=f?-1:0;for(b=b&512?1:0;b<e;b++)d[b]=c(d[b]);if(f){b=d[b]={};for(const g in f)b[g]=c(f[g])}Ia(d,a);return d};$a=function(a,b,c,d,e){if(a!=null){if(Array.isArray(a))a=Fa(a)?void 0:e&&(a[_.v]|0)&2?a:Za(a,b,c,d!==void 0,e);else if(Ea(a)){const f={};for(let g in a)f[g]=$a(a[g],b,c,d,e);a=f}else a=b(a,d);return a}};
Za=function(a,b,c,d,e){const f=d||c?a[_.v]|0:0;d=d?!!(f&32):void 0;const g=_.ya(a);for(let h=0;h<g.length;h++)g[h]=$a(g[h],b,c,d,e);c&&(Ia(g,a),c(f,g));return g};ab=function(a){return a.Fd===_.Sa?a.toJSON():Ua(a)};
bb=function(a,b,c=Ba){if(a!=null){if(a instanceof Uint8Array)return b?a:new Uint8Array(a);if(Array.isArray(a)){var d=a[_.v]|0;if(d&2)return a;b&&(b=d===0||!!(d&32)&&!(d&64||!(d&16)));return b?(a[_.v]=(d|34)&-12293,a):Za(a,bb,d&4?Ba:c,!0,!0)}a.Fd===_.Sa&&(c=a.ha,d=c[_.v],a=d&2?a:new a.constructor(_.cb(c,d,!0)));return a}};_.cb=function(a,b,c){const d=c||b&2?Ba:Aa,e=!!(b&32);a=Ya(a,b,f=>bb(f,e,d));a[_.v]=a[_.v]|32|(c?2:0);return a};
_.db=function(a){const b=a.ha,c=b[_.v];return c&2?new a.constructor(_.cb(b,c,!1)):a};eb=function(a){return a};fb=function(a){return a};jb=function(a,b,c,d){return gb(a,b,c,d,hb,ib)};mb=function(a,b,c,d){return gb(a,b,c,d,kb,lb)};
gb=function(a,b,c,d,e,f){if(!c.length&&!d)return 0;var g=0;let h=0,k=0;var l=0;let n=0;for(var p=c.length-1;p>=0;p--){var r=c[p];d&&p===c.length-1&&r===d||(l++,r!=null&&k++)}if(d)for(var q in d)p=+q,isNaN(p)||(n+=nb(p),h++,p>g&&(g=p));l=e(l,k)+f(h,g,n);q=k;p=h;r=g;let x=n;for(let D=c.length-1;D>=0;D--){var A=c[D];if(A==null||d&&D===c.length-1&&A===d)continue;A=D-b;const H=e(A,q)+f(p,r,x);H<l&&(a=1+A,l=H);p++;q--;x+=nb(A);r=Math.max(r,A)}b=e(0,0)+f(p,r,x);b<l&&(a=0,l=b);if(d){p=h;r=g;x=n;q=k;for(const D in d)d=
+D,isNaN(d)||d>=1024||(p--,q++,x-=D.length,g=e(d,q)+f(p,r,x),g<l&&(a=1+d,l=g))}return a};lb=function(a,b,c){return c+a*3+(a>1?a-1:0)};kb=function(a,b){return(a>1?a-1:0)+(a-b)*4};ib=function(a,b){return a==0?0:9*Math.max(1<<32-Math.clz32(a+a/2-1),4)<=b?a==0?0:a<4?100+(a-1)*16:a<6?148+(a-4)*16:a<12?244+(a-6)*16:a<22?436+(a-12)*19:a<44?820+(a-22)*17:52+32*a:40+4*b};hb=function(a){return 40+4*a};nb=function(a){return a>=100?a>=1E4?Math.ceil(Math.log10(1+a)):a<1E3?3:4:a<10?1:2};
_.ob=function(a,b,c,d){var e;d=(e=d)!=null?e:0;if(a==null)e=96,c?(a=[c],e|=512):a=[],b&&(e=e&-33521665|(b&1023)<<15);else{if(!Array.isArray(a))throw Error("t");e=a[_.v]|0;if(e&2048)throw Error("w");if(e&64)return a;d===1||d===2||(e|=64);if(c&&(e|=512,c!==a[0]))throw Error("x");a:{d=a;c=e;if(e=d.length){const f=e-1;if(Ea(d[f])){c|=256;b=f-(+!!(c&512)-1);if(b>=1024)throw Error("y");e=c&-33521665|(b&1023)<<15;break a}}if(b){b=Math.max(b,e-(+!!(c&512)-1));if(b>1024)throw Error("z");e=c&-33521665|(b&1023)<<
15}else e=c}}a[_.v]=e;return a};pb=function(a,b,c,d){b=d+(+!!(b&512)-1);if(!(b<0||b>=a.length||b>=c))return a[b]};_.qb=function(a,b,c,d){const e=b>>15&1023||536870912;if(c>=e){let f,g=b;if(b&256)f=a[a.length-1];else{if(d==null)return g;f=a[e+(+!!(b&512)-1)]={};g|=256}f[c]=d;c<e&&(a[c+(+!!(b&512)-1)]=void 0);g!==b&&(a[_.v]=g);return g}a[c+(+!!(b&512)-1)]=d;b&256&&(a=a[a.length-1],c in a&&delete a[c]);return b};
_.sb=function(a,b,c,d){a=a.ha;let e=a[_.v];d=_.rb(a,e,c,d);b=_.Ta(d,b,e);b!==d&&b!=null&&_.qb(a,e,c,b);return b};_.tb=function(a,b){return a!=null?a:b};
wb=function(a){var b=a.ha;b=ub?b:Za(b,ab,void 0,void 0,!1);var c=!ub,d=(c?a.ha:b)[_.v];if(a=b.length){var e=b[a-1],f=Ea(e);f?a--:e=void 0;var g=+!!(d&512)-1,h=a-g;d=!!vb&&!(d&512);var k,l=(k=vb)!=null?k:fb;k=d?l(h,g,b,e):h;d=(h=d&&h!==k)?Array.prototype.slice.call(b,0,a):b;if(f||h){b:{var n=d;var p=e;var r;f=!1;if(h)for(l=Math.max(0,k+g);l<n.length;l++){var q=n[l];const D=l-g;if(!(q==null||Fa(q)||Da(q)&&q.size===0)){var x=n[l]=void 0;((x=r)!=null?x:r={})[D]=q;f=!0}}if(p)for(let D in p)if(x=+D,isNaN(x)){let H;
((H=r)!=null?H:r={})[D]=p[D]}else if(l=p[D],Array.isArray(l)&&(Fa(l)||Da(l)&&l.size===0)&&(l=null),l==null&&(f=!0),h&&x<k){f=!0;l=x+g;for(q=n.length;q<=l;q++)n.push(void 0);n[l]=p[x]}else if(l!=null){let H;((H=r)!=null?H:r={})[D]=l}f||(r=p);if(r)for(let D in r){p=r;break b}p=null}n=p==null?e!=null:p!==e}h&&(a=d.length);for(;a>0;a--){r=d[a-1];if(!(r==null||Fa(r)||Da(r)&&r.size===0))break;var A=!0}if(d!==b||n||A){if(!h&&!c)d=Array.prototype.slice.call(d,0,a);else if(A||n||p)d.length=a;p&&d.push(p)}A=
d}else A=b;return A};_.xb=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.w=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.yb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.zb=function(a){for(const b in a)return!1;return!0};Ab=Object.defineProperty;
Bb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Cb=Bb(this);Db=function(a,b){if(b)a:{var c=Cb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Ab(c,a,{configurable:!0,writable:!0,value:b})}};
Db("Symbol.dispose",function(a){return a?a:Symbol("b")});Db("globalThis",function(a){return a||Cb});Db("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});var Fb,Jb;_.Eb=_.Eb||{};_.t=this||self;Fb=_.t._F_toggles||[];_.Gb=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Ma=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Hb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Ib="closure_uid_"+(Math.random()*1E9>>>0);Jb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Jb;return _.z.apply(null,arguments)};
_.Kb=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.B=function(a,b){a=a.split(".");var c=_.t;a[0]in c||typeof c.execScript=="undefined"||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};
_.C=function(a,b){function c(){}c.prototype=b.prototype;a.W=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.zj=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.C(_.aa,Error);_.aa.prototype.name="CustomError";var Lb=!!(Fb[0]&2048);var Mb;if(Fb[0]&1024)Mb=Lb;else{var Nb=_.Gb("WIZ_global_data.oxN3nb"),Ob=Nb&&Nb[610401301];Mb=Ob!=null?Ob:!1}var fa=Mb;_.Pb=_.ba(a=>typeof a==="number");_.Qb=_.ba(a=>typeof a==="string");_.Rb=_.ba(a=>typeof a==="boolean");_.Sb=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Vb,Tb,Wb,Ub;_.Wa=_.ba(a=>_.Sb?a>=Tb&&a<=Ub:a[0]==="-"?ca(a,Vb):ca(a,Wb));Vb=Number.MIN_SAFE_INTEGER.toString();Tb=_.Sb?BigInt(Number.MIN_SAFE_INTEGER):void 0;Wb=Number.MAX_SAFE_INTEGER.toString();Ub=_.Sb?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Xb=typeof TextDecoder!=="undefined";_.Yb=typeof TextEncoder!=="undefined";_.Zb=function(){return _.ea().toLowerCase().indexOf("webkit")!=-1};var ia,$b=_.t.navigator;ia=$b?$b.userAgentData||null:null;_.ua=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.ac=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.bc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.cc=function(a){_.cc[" "](a);return a};_.cc[" "]=function(){};var pc;_.dc=_.la();_.ec=_.ma();_.fc=_.u("Edge");_.gc=_.u("Gecko")&&!(_.Zb()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.hc=_.Zb()&&!_.u("Edge");_.ic=_.ta();_.jc=qa()?ia.platform==="Windows":_.u("Windows");_.kc=qa()?ia.platform==="Android":_.u("Android");_.lc=ra();_.mc=_.u("iPad");_.nc=_.u("iPod");_.oc=_.sa();
a:{let a="";const b=function(){const c=_.ea();if(_.gc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.fc)return/Edge\/([\d\.]+)/.exec(c);if(_.ec)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.hc)return/WebKit\/(\S+)/.exec(c);if(_.dc)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.ec){var qc;const c=_.t.document;qc=c?c.documentMode:void 0;if(qc!=null&&qc>parseFloat(a)){pc=String(qc);break a}}pc=a}_.rc=pc;_.sc=_.na();_.tc=ra()||_.u("iPod");_.uc=_.u("iPad");_.vc=_.u("Android")&&!(oa()||_.na()||_.la()||_.u("Silk"));_.wc=oa();_.xc=_.pa()&&!_.sa();var yc;_.v=Symbol();yc=Symbol();_.zc=Symbol();var Ca,Bc;_.Sa={};Ca={};Bc=[];Bc[_.v]=55;_.Ac=Object.freeze(Bc);_.Cc=Object.freeze({});var Ja=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};var Dc;_.Ec=function(a,b){a=a.ha;return _.rb(a,a[_.v],b)};_.rb=function(a,b,c,d){if(c===-1)return null;const e=b>>15&1023||536870912;if(c>=e){if(b&256)return a[a.length-1][c]}else{var f=a.length;if(d&&b&256&&(d=a[f-1][c],d!=null)){if(pb(a,b,e,c)&&yc!=null){var g;a=(g=Dc)!=null?g:Dc={};g=a[yc]||0;g>=4||(a[yc]=g+1,_.Ka())}return d}return pb(a,b,e,c)}};_.Fc=function(a,b,c){const d=a.ha;let e=d[_.v];_.Ga(e);_.qb(d,e,b,c);return a};
_.E=function(a,b,c,d=!1){b=_.sb(a,b,c,d);if(b==null)return b;a=a.ha;d=a[_.v];if(!(d&2)){const e=_.db(b);e!==b&&(b=e,_.qb(a,d,c,b))}return b};_.F=function(a,b,c){c==null&&(c=void 0);return _.Fc(a,b,c)};_.G=function(a,b){a=_.Ec(a,b);return a==null||typeof a==="boolean"?a:typeof a==="number"?!!a:void 0};_.I=function(a,b){return _.Ra(_.Ec(a,b))};_.J=function(a,b,c=!1){return _.tb(_.G(a,b),c)};_.K=function(a,b){return _.tb(_.I(a,b),"")};_.M=function(a,b,c){return _.Fc(a,b,c==null?c:_.Na(c))};
_.N=function(a,b,c){return _.Fc(a,b,c==null?c:_.Pa(c))};_.O=function(a,b,c){return _.Fc(a,b,_.Qa(c))};_.P=function(a,b,c){return _.Fc(a,b,c==null?c:_.Oa(c))};var vb,ub;_.Q=class{constructor(a,b,c){this.ha=_.ob(a,b,c)}toJSON(){return wb(this)}Aa(a){try{return ub=!0,a&&(vb=a===fb||a!==eb&&a!==jb&&a!==mb?fb:a),JSON.stringify(wb(this),Va)}finally{a&&(vb=void 0),ub=!1}}oc(){return _.za(this.ha)}};_.Q.prototype.Fd=_.Sa;_.Q.prototype.toString=function(){try{return ub=!0,wb(this).toString()}finally{ub=!1}};_.Ic=_.xb();_.Jc=_.xb();_.Kc=_.xb();var Lc=class extends _.Q{constructor(a){super(a)}};_.Mc=class extends _.Q{constructor(a){super(a)}D(a){return _.N(this,3,a)}};var Nc=class extends _.Q{constructor(a){super(a)}Ic(a){return _.O(this,24,a)}};_.Oc=class extends _.Q{constructor(a){super(a)}};_.R=function(){this.qa=this.qa;this.Y=this.Y};_.R.prototype.qa=!1;_.R.prototype.isDisposed=function(){return this.qa};_.R.prototype.dispose=function(){this.qa||(this.qa=!0,this.O())};_.R.prototype[Symbol.dispose]=function(){this.dispose()};_.R.prototype.O=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Pc=class extends _.R{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}tb(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].tb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Rc=class extends _.R{constructor(){var a=_.Qc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Sc=class extends _.Q{constructor(a){super(a)}};var Tc=class extends _.Q{constructor(a){super(a)}};var Wc;_.Uc=function(a,b,c=98,d=new _.Mc){if(a.i){const e=new Lc;_.O(e,1,b.message);_.O(e,2,b.stack);_.N(e,3,b.lineNumber);_.P(e,5,1);_.F(d,40,e);a.i.log(c,d)}};Wc=class{constructor(){var a=Vc;this.i=null;_.J(a,4,!0)}log(a,b,c=new _.Mc){_.Uc(this,a,98,c)}};var Xc,Yc;Xc=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.ac(c,b,a)}catch(d){console.error(d)}}}};_.Zc=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new Yc(a,b,c));Xc(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("D");this.i=a;Xc(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("D");this.j=a;Xc(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
Yc=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.$c=a=>{var b="lc";if(a.lc&&a.hasOwnProperty(b))return a.lc;b=new a;return a.lc=b};_.ad=class{constructor(){this.v=new _.Zc;this.i=new _.Zc;this.D=new _.Zc;this.B=new _.Zc;this.C=new _.Zc;this.A=new _.Zc;this.o=new _.Zc;this.j=new _.Zc;this.F=new _.Zc}Y(){return this.v}M(){return this.i}N(){return this.D}L(){return this.B}qa(){return this.C}K(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.$c(_.ad)}};var ed;_.cd=function(){return _.E(_.bd,Nc,1)};_.dd=function(){return _.E(_.bd,_.Oc,5)};ed=class extends _.Q{constructor(a){super(a)}};var fd;window.gbar_&&window.gbar_.CONFIG?fd=window.gbar_.CONFIG[0]||{}:fd=[];_.bd=new ed(fd);var Vc=_.E(_.bd,Tc,3)||new Tc;_.cd()||new Nc;_.Qc=new Wc;_.B("gbar_._DumpException",function(a){_.Qc?_.Qc.log(a):console.error(a)});_.gd=new Rc;var id;_.jd=function(a,b){var c=_.hd.i();if(a in c.i){if(c.i[a]!=b)throw new id;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.zb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.hd=class{constructor(){this.i={};this.j={}}static i(){return _.$c(_.hd)}};_.kd=class extends _.aa{constructor(){super()}};id=class extends _.kd{};_.B("gbar.A",_.Zc);_.Zc.prototype.aa=_.Zc.prototype.then;_.B("gbar.B",_.ad);_.ad.prototype.ba=_.ad.prototype.M;_.ad.prototype.bb=_.ad.prototype.N;_.ad.prototype.bd=_.ad.prototype.qa;_.ad.prototype.bf=_.ad.prototype.Y;_.ad.prototype.bg=_.ad.prototype.L;_.ad.prototype.bh=_.ad.prototype.K;_.ad.prototype.bj=_.ad.prototype.J;_.ad.prototype.bk=_.ad.prototype.G;_.B("gbar.a",_.ad.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var ld=new Pc;_.jd("api",ld);
var md=_.dd()||new _.Oc,nd=window,pd=_.y(_.I(md,8));nd.__PVT=pd;_.jd("eq",_.gd);
}catch(e){_._DumpException(e)}
try{
_.qd=class extends _.Q{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var rd=class extends _.Q{constructor(a){super(a)}};var sd=class extends _.R{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.I(a,1));_.G(a,12)!=null&&(d.dpo=_.w(_.J(a,12)));d.ms=_.y(_.I(a,2));d.m=_.y(_.I(a,3));d.l=[];_.K(b,1)&&(a=_.I(b,3))&&this.i.push(a);_.K(c,1)&&(c=_.I(c,2))&&this.i.push(c);_.B("gapi.load",(0,_.z)(this.o,this));return this}};var td=_.E(_.bd,_.Sc,14);if(td){var ud=_.E(_.bd,_.qd,9)||new _.qd,vd=new rd,wd=new sd;wd.init(td,ud,vd);_.jd("gs",wd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_sunnyrockzzmadani@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./python_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20250102-060136_RC00_711390485'; var colabScsVersion = '033d4b5a17e7acf4dcfed99acc563065'; var hl = 'en'; var colabExperiments = JSON.parse('\x7b\x22add_prompt_cell\x22: false, \x22ai_banner\x22: false, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 2000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_do_conversation_model_id\x22: \x22\x22, \x22aida_generate_code_model_id\x22: \x22\x22, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22auto_open_chat_on_empty_notebook\x22: false, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22cell_markdown_toolbar_tooltips\x22: true, \x22cell_output_actions_tooltip\x22: true, \x22cell_tags\x22: false, \x22cell_toolbar_ai_menu\x22: true, \x22cell_toolbar_tooltips\x22: true, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22chat_reduce_refusals\x22: true, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: true, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22code_report_millis\x22: 600000, \x22commands_in_toolbar\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22compose_skip_suffix_check\x22: false, \x22converse_server_side_history\x22: false, \x22converse_temp\x22: \x22\x22, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22dbu\x22: \x22\x22, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22development\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_completions_backend_switching\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_rt_on_create\x22: false, \x22execution_announcements\x22: true, \x22execution_status_propagation\x22: true, \x22explain_cell\x22: true, \x22explain_error\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22filter_repetitive_suggestions\x22: false, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22gemini_rebrand\x22: true, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_duplicate_code\x22: true, \x22generate_prompt_reduce_name_errors\x22: false, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22granular_browser_permissions\x22: true, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22i18n_runtime_labels\x22: false, \x22import_data\x22: false, \x22import_gemini_api_key\x22: true, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22interactive_sheet_next_steps\x22: true, \x22internal_chat\x22: false, \x22internal_schedule\x22: false, \x22is_prober\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22key_promoter\x22: false, \x22kr\x22: false, \x22last_saved_indicator_refresh\x22: false, \x22latest_notebook_context_for_converse\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22minimizable_comments\x22: true, \x22ml_enabled\x22: true, \x22mlpp_multiline\x22: false, \x22mobile\x22: false, \x22move_converse_notebook_context_to_facts\x22: true, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22notebook_context_length\x22: 40000, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prereq_cells_next_steps\x22: true, \x22prompt_for_dsa_trusted_tester_consent\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kws\x22: false, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: false, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_serving_config\x22: \x22pl_700m_smart_paste_3.0.25\x22, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22task_service_max_poll_count\x22: 45, \x22task_service_poll_interval_ms\x22: 2000, \x22task_service_wait_before_polling_ms\x22: 5000, \x22term4all\x22: false, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22tpu_v5e1\x22: true, \x22transform_code\x22: false, \x22transform_code_context_file_per_cell\x22: false, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22updated_inline_cell_diff\x22: false, \x22use_corplogin\x22: true, \x22use_dm_sql_lsp\x22: false, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22want_completions_ai_consent_campaign\x22: false, \x22workstations\x22: false, \x22ids\x22: \x5b20730345, 20730177, 20730351, 20730297, 20730357, 20730150, 20730186, 20730183, 20730330, 20730265, 20730230, 20730262, 20730252, 20730324, 20730315, 20730318\x5d, \x22flag_ids\x22: \x7b\x22add_prompt_cell\x22: 45644995, \x22ai_banner\x22: 45670540, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_generate_code_model_id\x22: 45427663, \x22allowed_public_url_domains\x22: 45425558, \x22auto_open_chat_on_empty_notebook\x22: 45669599, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22cell_markdown_toolbar_tooltips\x22: 45654223, \x22cell_output_actions_tooltip\x22: 45650940, \x22cell_tags\x22: 45425779, \x22cell_toolbar_ai_menu\x22: 45647581, \x22cell_toolbar_tooltips\x22: 45649981, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22chat_reduce_refusals\x22: 45656767, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22code_report_millis\x22: 45658073, \x22commands_in_toolbar\x22: 45425502, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22compose_skip_suffix_check\x22: 45615470, \x22converse_server_side_history\x22: 45634472, \x22converse_temp\x22: 45425509, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22dbu\x22: 45425545, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22development\x22: 45425544, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22enable_adhoc_backends\x22: 45425506, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_completions_backend_switching\x22: 45662651, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_rt_on_create\x22: 45667583, \x22execution_announcements\x22: 45651325, \x22execution_status_propagation\x22: 45644828, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22gemini_rebrand\x22: 45631310, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_duplicate_code\x22: 45646291, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22granular_browser_permissions\x22: 45630936, \x22hats_surveys\x22: 45425559, \x22i18n_runtime_labels\x22: 45662916, \x22import_data\x22: 45430411, \x22import_gemini_api_key\x22: 45654551, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22interactive_sheet_next_steps\x22: 45634324, \x22internal_chat\x22: 45622872, \x22internal_schedule\x22: 45425578, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22key_promoter\x22: 45425570, \x22last_saved_indicator_refresh\x22: 45672240, \x22latest_notebook_context_for_converse\x22: 45668776, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22minimizable_comments\x22: 45661083, \x22ml_enabled\x22: 45425493, \x22mlpp_multiline\x22: 45425623, \x22mobile\x22: 45425562, \x22move_converse_notebook_context_to_facts\x22: 45666389, \x22mpp_orc_temperature_override\x22: 45649914, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22notebook_context_length\x22: 45633457, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prereq_cells_next_steps\x22: 45640400, \x22prompt_for_dsa_trusted_tester_consent\x22: 45670923, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kws\x22: 45650184, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22tpu_v5e1\x22: 45652002, \x22transform_code\x22: 45667102, \x22transform_code_context_file_per_cell\x22: 45671260, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22updated_inline_cell_diff\x22: 45667103, \x22use_corplogin\x22: 45425606, \x22use_dm_sql_lsp\x22: 45425610, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22want_completions_ai_consent_campaign\x22: 45671138, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'sunnyrockzzmadani@gmail.com'; var colabRenderDataToken = 'AFWLbD0JUAOxqlFyTo6l1BAQ0b_IWBpf41rASrne-vKsu_T1qQN98omG2CTy-busW2KfwjQTAB8ZGSCjsk0HZ4V_v9HjbLSp_Ben'; var colabConfig = '\x5b\x5b\x22sunnyrockzzmadani@gmail.com\x22,\x5b1,\x22AHXL0D3tnnEmdkdCWtg0hlFKfU9Kcb9jP97IrUQdseivexSJ0vvQma7SlJSVGl4i6szP0vZo2uLLM9DOX6W59rx\/EsXkcOs9CxSsRENlgx8ZgIpFre+Xh+PkASG12eM0WonPxr1qfqt5ryDn4h8Dmepxb48l\/BXq9IZ0Z7eEjaXqzXs3QVnV7KO2Mx+HFKLd5bhThKgqSANHSjC\/Uy4324SsJZoLSCz\/WwUorW3MNRTUZOYRHxt8olW3tc6shWfpKkSa6naFHuBT7pQ1KyskPhMDBQkL294BkiJSfyGfkJAdIWX\/ryC4F2WPizTyMllqKDUlXxFwu+jame8ILhVQGOwHxTpuEYoIWYgUkF\/WmLg+7nHSN0m2HBY2RtwzbeCPvt9oCdRmwBmxTk6ZtkaZaEBNOuQP9wly6T52p0M6tor8ddDAdxZ94GlmWS+XVRFrllCv4CXCmIMWsZPfB\/Y+oktQHpqAQglJWHR3UIqGn7FPcvtdyPyJ+T3BtJd+iqcI7lHnyn182xUGlAb30aCsEuST6j18UG2btDoIN4KUxGG7aifZLhx0YLaxQiuxfTPwlbBxA0vQHmumFygvjyufK8wtLgwXcXlxxDvt4GDLARoQOhP6PwhGpbrJWjDhOmZtVZZDVJgqLfzVFFeogDLu8m+yUulodNWxuKiuaKA3xoPkMTtobJkLqWvUSg4aaS4mqdXHeUrUrb+xV1hE9BxIGEs\/qP7d1SfjY0oyC+hs2CJA9edHQsKjIZEyXC4ob\/oN0hU7HyeX62Zc0imeAEHXJqq0p54QlrVJWjwKypCKXXA29EtSlBEU8bj5tb0f5yJfouDilbUfnK7YSoFi\/Th2MZPSa4biS14nK2snIhwlULYNL2DMene8NB\/YaFsjWdnSNVe132sdJmSTwx7MdHG2yB8YNQ+Sup59vmfLiX3zIiCvEXSz3yaH5Bqf7sX3lbfipZkHwcHUR7FhB2Z\/CFqdb7peRVJXP2a7OvYHhW7w6fNjF8QWv4diLEh7RNNOMVeOBIRMRKxM75QwgbZA8ZfDQpE6Wg4SttekpcglKWrlbv86fpqLiL3yyZpSmnCK5PgRpyM6qBpN5UffmQpEBFF445w3+tk\/P+Ns9lqrE5H\/krw0UCyk1O4F4X3cSvjnfUc3Ojn8mMBmvYg5xq0k4MHSRagEvgcSSCxJR8q1wDI3iCKlg0qLysmbe34lWKwRLlzy9rvOFMCXle3L65YxWgW7fD\/GuaTCrA2raxFSN9AnP4f6qsBLV0AV8TBt\/JibQkvr0M8QC7vdcAISxYylwAgGpqeJqeqDus\/KzrdSxZRUS2\/G6+d7RfrZF95C23csyhjFR4nCuy4USL065I6CWxpHeNEuOej3\/jLjQB25\/FRPVbaXD+FdBU9bUujrrcZhtVaU7FDjxXv7OtcGePrk7P8b6G+PVd2fLpzk4hxRadoneujRtU+KCxMJehKnwE7AadfHjxfBMJygBzJBiftm+gosoh1sz3WfKMrG8azPaEs\/Qn5sXl1UHgipv+nU9n2sb5jjih+gmwZDYP6WTwVbgsDsF9Iuq5KmVIWLD6b2MdM9DxYEcaTQ7OB3kEtpjKP+321shoGUB7cXMLqTedPqoWJxmrFcxY4WmD\/wb3P8VuGA4Yb9oFD6jidhQkeBFDnbp4HJWiWpdZv5I+l7YAd\/e1Nhvb\/Va9GAj0w4XRPBynWtxIFu2WSaTvyOw+i4iDDoNkTq+vp65EfKZOIxuVhxPM9i3ZeXfpjsbN1SEc\/OA3KNciaRYMhzNMZRPGAJFFiczGGcv1v465hwx1COvlV+g7HL8q7xQgcNVCyzW0jOuq6K1u9wjEPI8ttz2cbZHisWEuff9Dh2dNUKF4AS4N8QzaSUJkWnM9ZNjb\/b1W+GduoqeF3lP6sZjTuS6tQ\x3d\x22,\x22AJ9oCCwqPmtzybnPcP\/SFTxuNj\/y0rGo7mOb65Dh4E5hC+jd5ss5CjRzDsZEu7tpERmi31fXA8rVS4HbY2F0LffvNgnCi2q4LgK8DPWAK+KVmqpiFXulIKrnIxUsUxvBqAY9kBaWkN10\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$11.79\x22,\x22$58.99\x22,\x22$11.79\x22,\x22$58.99\x22\x5d,\x5b1,5\x5d,\x22IN\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/033d4b5a17e7acf4dcfed99acc563065/img/favicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="-wL8iYJTC7X0zF9qBNDQUAd-P1ZkQUK-OhSgv4Wkf1M"><meta name="google-site-verification" content="o-EECwEDQeUpZv0jTmoGfCDX7dUI8Kul4ESepXmDnO0"><meta name="google-site-verification" content="sNOroO9gXrazN-oMODOm0Bs0_vw1R5QwZ-BfrSHn8Io"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="8P-D5fVWgUIhw8X2BxnKJbf5itK0zxX0QhoBjbJFTe8"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="v2MQvJk6wTiBarKTbe1mdivqYCVtw-5m6w0HDzV5X_4"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./python_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="async" type="text/javascript" src="./python_files/editor.main.js.download"></script><script async="" type="text/javascript" charset="UTF-8" src="./python_files/rs=AA2YrTu0yU9RTMfNNC-LVUmaaNKwIO136g" nonce=""></script><link type="text/css" href="./python_files/rs=AA2YrTs4SLbgh5FvGZPW_Ny7TyTdXfy6xA" rel="stylesheet"><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./python_files/editor.main.css"><script async="async" type="text/javascript" src="./python_files/editor.main.nls.js.download"></script><script async="async" type="text/javascript" src="./python_files/markdown.js.download"></script><script src="./python_files/api.js.download" nonce=""></script><script src="./python_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #1e1e1e; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #1e1e1e;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #1e1e1e;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: rgba(156, 204, 44, 0.13);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.14);
--vscode-diffEditor-insertedLineBackground: rgba(156, 204, 44, 0.13);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.14);
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #1e1e1e;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #1e1e1e;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #1e1e1e;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #1e1e1e; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #6aa94f; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #f28b82; }
.mtk11 { color: #d7ba7d; }
.mtk12 { color: #dcdcdc; }
.mtk13 { color: #808080; }
.mtk14 { color: #4ec9b0; }
.mtk15 { color: #dcdcaa; }
.mtk16 { color: #f44747; }
.mtk17 { color: #82c6ff; }
.mtk18 { color: #c586c0; }
.mtk19 { color: #a79873; }
.mtk20 { color: #dd6a6f; }
.mtk21 { color: #5bb498; }
.mtk22 { color: #909090; }
.mtk23 { color: #778899; }
.mtk24 { color: #ff00ff; }
.mtk25 { color: #b46695; }
.mtk26 { color: #ff0000; }
.mtk27 { color: #4f76ac; }
.mtk28 { color: #3dc9b0; }
.mtk29 { color: #74b0df; }
.mtk30 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style></head><body class="" style="overflow: hidden;"><div inert="" aria-hidden="true" style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" inert="" aria-hidden="true" style="display: none;"></div><div class="scripts" inert="" aria-hidden="true"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./python_files/gapi_loader.js.download" nonce=""></script><script src="./python_files/socketio_binary.js.download" nonce=""></script><script src="./python_files/analytics_binary.js.download" nonce=""></script><script src="./python_files/MathJax.js.download" nonce=""></script><script src="./python_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./python_files/external_binary.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area" inert="" aria-hidden="true"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$040125974$-->
      <div class="mdc-snackbar  mdc-snackbar--leading ">
        <div class="mdc-snackbar__surface">
          <!--?lit$040125974$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup" inert="" aria-hidden="true"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$040125974$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$040125974$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable="" inert="" aria-hidden="true"></div><div class="gb_R" ng-non-bindable="" inert="" aria-hidden="true"><div class="gb_Ac"><div>Google Account</div><div class="gb_g">madani roshan</div><div>sunnyrockzzmadani@gmail.com</div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Bd;Bd=class extends _.kd{};_.Cd=function(a,b){if(b in a.i)return a.i[b];throw new Bd;};_.Dd=function(a){return _.Cd(_.hd.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Gd;_.Ed=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Gd=function(a){return new _.Fd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Hd=globalThis.trustedTypes;_.Id=class{constructor(a){this.i=a}toString(){return this.i}};_.Jd=new _.Id("about:invalid#zClosurez");_.Fd=class{constructor(a){this.nh=a}};_.Kd=[Gd("data"),Gd("http"),Gd("https"),Gd("mailto"),Gd("ftp"),new _.Fd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Ld=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Md=new _.Ld(_.Hd?_.Hd.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Qd,de,Pd,Rd,Wd;_.Nd=function(a){return a==null?a:Number.isFinite(a)?a|0:void 0};_.Od=function(a){if(a==null)return a;if(typeof a==="string"){if(!a)return;a=+a}if(typeof a==="number")return Number.isFinite(a)?a|0:void 0};Qd=function(){let a=null;if(!Pd)return a;try{const b=c=>c;a=Pd.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Sd=function(){Rd===void 0&&(Rd=Qd());return Rd};
_.Ud=function(a){const b=_.Sd();return new _.Td(b?b.createScriptURL(a):a)};_.Vd=function(a){if(a instanceof _.Td)return a.i;throw Error("F");};_.Xd=function(a){if(Wd.test(a))return a};_.Yd=function(a){if(a instanceof _.Id)if(a instanceof _.Id)a=a.i;else throw Error("F");else a=_.Xd(a);return a};_.Zd=function(a,b=document){let c,d;b=(d=(c="document"in b?b.document:b).querySelector)==null?void 0:d.call(c,`${a}[nonce]`);return b==null?"":b.nonce||b.getAttribute("nonce")||""};
_.$d=function(a){var b=_.Ma(a);return b=="array"||b=="object"&&typeof a.length=="number"};_.ae=function(a,b,c){return _.sb(a,b,c,!1)!==void 0};_.be=function(a,b){return _.Od(_.Ec(a,b))};_.S=function(a,b){return _.Nd(_.Ec(a,b))};_.T=function(a,b,c=0){return _.tb(_.be(a,b),c)};_.ce=function(a,b,c=0){return _.tb(_.S(a,b),c)};_.ee=function(a,b){return a.lastIndexOf(b,0)==0};Pd=_.Hd;_.Td=class{constructor(a){this.i=a}toString(){return this.i+""}};Wd=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var je,ne,fe;_.he=function(a){return a?new fe(_.ge(a)):de||(de=new fe)};_.ie=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.U=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a?a=(b||c).querySelector(a?"."+a:""):(b=b||c,a=(a?b.querySelectorAll(a?"."+a:""):b.getElementsByTagName("*"))[0]||null));return a||null};
_.ke=function(a,b){_.yb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:je.hasOwnProperty(d)?a.setAttribute(je[d],c):_.ee(d,"aria-")||_.ee(d,"data-")?a.setAttribute(d,c):a[d]=c})};je={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.le=function(a){return a?a.defaultView:window};_.oe=function(a,b){const c=b[1],d=_.me(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.ke(d,c));b.length>2&&ne(a,d,b);return d};ne=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.$d(f)||_.Hb(f)&&f.nodeType>0?d(f):_.ac(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Ed(f):f,d)}};
_.pe=function(a){return _.me(document,a)};_.me=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.qe=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.re=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.se=function(a,b){return a&&b?a==b||a.contains(b):!1};_.ge=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};fe=function(a){this.i=a||_.t.document||document};_.m=fe.prototype;
_.m.H=function(a){return _.ie(this.i,a)};_.m.Wa=function(a,b,c){return _.oe(this.i,arguments)};_.m.appendChild=function(a,b){a.appendChild(b)};_.m.xe=_.qe;_.m.Sf=_.re;_.m.Rf=_.se;
}catch(e){_._DumpException(e)}
try{
_.Ci=function(a){const b=_.Zd("script",a.ownerDocument&&a.ownerDocument.defaultView||window);b&&a.setAttribute("nonce",b)};_.Di=function(a){if(!a)return null;a=_.I(a,4);var b;a===null||a===void 0?b=null:b=_.Ud(a);return b};_.Ei=class extends _.Q{constructor(a){super(a)}};_.Fi=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Hi=function(a,b,c){a<b?Gi(a+1,b):_.Qc.log(Error("da`"+a+"`"+b),{url:c})},Gi=function(a,b){if(Ii){const c=_.pe("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.Vd(Ii);_.Ci(c);c.onerror=_.Kb(Hi,a,b,c.src);_.Fi("HEAD")[0].appendChild(c)}},Ji=class extends _.Q{constructor(a){super(a)}};var Ki=_.E(_.bd,Ji,17)||new Ji,Li,Ii=(Li=_.E(Ki,_.Ei,1))?_.Di(Li):null,Mi,Ni=(Mi=_.E(Ki,_.Ei,2))?_.Di(Mi):null,Oi=function(){Gi(1,2);if(Ni){const a=_.pe("LINK");a.setAttribute("type","text/css");a.href=_.Vd(Ni).toString();a.rel="stylesheet";let b=_.Zd("style",window);b&&a.setAttribute("nonce",b);_.Fi("HEAD")[0].appendChild(a)}};(function(){const a=_.cd();if(_.G(a,18))Oi();else{const b=_.be(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Oi,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><mwc-dialog class="colab-side-tab-dialog very-wide colab-open-dialog" open=""><template shadowrootmode="open"><!---->
    <div role="dialog" aria-modal="true" class="mdc-dialog mdc-dialog--open" aria-label="Open notebook">
      <div class="mdc-dialog__container">
        <div class="mdc-dialog__surface">
          <!--?lit$040125974$-->
      <h2 id="title" class="mdc-dialog__title" style="border-top-width: 5px; border-image: linear-gradient(135deg, var(--colab-logo-dark) 0%, var(--colab-logo-dark) 5%, var(--colab-logo-light) 5%, var(--colab-logo-light) 75%, var(--colab-logo-dark) 75%, var(--colab-logo-dark) 100%) 1; border-top-style: solid;"><!--?lit$040125974$-->Open notebook</h2>
          <div id="content" class="mdc-dialog__content" style="padding: 0px;">
            <slot id="contentSlot"></slot>
          </div>
          <footer id="actions" class=" mdc-dialog__actions ">
            <span>
              <slot name="secondaryAction"></slot>
            </span>
            <span>
             <slot name="primaryAction"></slot>
            </span>
          </footer>
        </div>
      </div>
      <div class="mdc-dialog__scrim"></div>
    </div></template><!----><!----> <div class="dialog-content">
    <colab-side-tab-dialog-page-viewer insubmenu=""><template shadowrootmode="open"><!---->
      <div class="back">
        <mwc-button alt="Back"><template shadowrootmode="open"><!---->
      <button id="button" class="mdc-button   " aria-label="">
        <!--?lit$040125974$--><!--?-->
        <!--?lit$040125974$-->
        <span class="leading-icon">
          <slot name="icon">
            <!--?lit$040125974$-->
          </slot>
        </span>
        <span class="mdc-button__label"><!--?lit$040125974$--></span>
        <span class="slot-container   ">
          <slot></slot>
        </span>
        <span class="trailing-icon">
          <slot name="trailingIcon">
            <!--?lit$040125974$-->
          </slot>
        </span>
      </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_back</md-icon>
          <!--?lit$040125974$-->Back
        </mwc-button>
      </div>
      <div class="main-content">
        <md-list id="headings-menu"><template shadowrootmode="open"><!---->
      <slot>
      </slot>
    </template>
          <slot name="headings"></slot>
        </md-list>
        <slot name="pagecontent"></slot>
      </div>
    </template>
      <!--?lit$040125974$--><!---->
      <md-list-item type="button" slot="headings" md-list-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <button id="item" role="listitem" tabindex="0" class="list-item   "><!--?lit$040125974$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$040125974$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple> <!--?lit$040125974$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$040125974$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </button>
    </template>
        <span><!--?lit$040125974$-->Examples</span>
        <md-icon slot="end" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>chevron_right</md-icon>
      </md-list-item>
    <!----><!---->
      <md-list-item type="button" slot="headings" dialoginitialfocus="" md-list-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <button id="item" role="listitem" tabindex="0" class="list-item   "><!--?lit$040125974$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$040125974$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple> <!--?lit$040125974$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$040125974$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </button>
    </template>
        <span><!--?lit$040125974$-->Recent</span>
        <md-icon slot="end" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>chevron_right</md-icon>
      </md-list-item>
    <!----><!---->
      <md-list-item type="button" slot="headings" md-list-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <button id="item" role="listitem" tabindex="0" class="list-item   "><!--?lit$040125974$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$040125974$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple> <!--?lit$040125974$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$040125974$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </button>
    </template>
        <span><!--?lit$040125974$-->Google Drive</span>
        <md-icon slot="end" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>chevron_right</md-icon>
      </md-list-item>
    <!----><!---->
      <md-list-item type="button" slot="headings" md-list-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <button id="item" role="listitem" tabindex="0" class="list-item   "><!--?lit$040125974$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$040125974$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple> <!--?lit$040125974$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$040125974$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </button>
    </template>
        <span><!--?lit$040125974$-->GitHub</span>
        <md-icon slot="end" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>chevron_right</md-icon>
      </md-list-item>
    <!----><!---->
      <md-list-item type="button" slot="headings" md-list-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <button id="item" role="listitem" tabindex="0" class="list-item   "><!--?lit$040125974$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$040125974$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$040125974$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$040125974$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </button>
    </template>
        <span><!--?lit$040125974$-->Upload</span>
        <md-icon slot="end" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>chevron_right</md-icon>
      </md-list-item>
    <!---->

      <colab-pages slot="pagecontent" class="colab-styled-scroller" selected="1"><template shadowrootmode="open"><!----><slot name="page-0"></slot></template>
        <!--?lit$040125974$--><!----><div class="pagecontent right-content selected-tab" slot="page-0">
      <!----><!--?lit$040125974$--><!--?lit$040125974$--><colab-notebook-list><template shadowrootmode="open"><!----> <div class="dialog-table-container">
      <section class="dialog-table-input-row">
        <md-outlined-text-field id="dialog-table-filter-input" label="Search notebooks" data-aria-label="Enter a search string to filter the list of notebooks shown below." inputmode="" type="text" autocomplete=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <span class="text-field   ">
        <!--?lit$040125974$--><md-outlined-field class="field" count="0" error-text="" label="Search notebooks" max="-1" supporting-text="" has-end=""><template shadowrootmode="open"><!---->
      <div class="field with-end">
        <div class="container-overflow">
          <!--?lit$040125974$-->
          <slot name="container"></slot>
          <!--?lit$040125974$--> <!--?lit$040125974$--> <!--?lit$040125974$-->
      <div class="outline">
        <div class="outline-start"></div>
        <div class="outline-notch">
          <div class="outline-panel-inactive"></div>
          <div class="outline-panel-active"></div>
          <div class="outline-label"><!--?lit$040125974$-->
      <span class="label  hidden floating " aria-hidden="true"><!--?lit$040125974$-->Search notebooks</span>
    </div>
        </div>
        <div class="outline-end"></div>
      </div>
    
          <div class="container">
            <div class="start">
              <slot name="start"></slot>
            </div>
            <div class="middle">
              <div class="label-wrapper">
                <!--?lit$040125974$-->
      <span class="label  resting " aria-hidden="false"><!--?lit$040125974$-->Search notebooks</span>
     <!--?lit$040125974$-->
              </div>
              <div class="content">
                <slot></slot>
              </div>
            </div>
            <div class="end">
              <slot name="end"></slot>
            </div>
          </div>
        </div>
        <!--?lit$040125974$-->
      </div>
    </template>
      <!--?lit$040125974$-->
      <span class="icon leading" slot="start">
        <slot name="leading-icon"></slot>
      </span>
    
      <!--?lit$040125974$-->
      <div class="input-wrapper">
        <!--?lit$040125974$-->
        <input class="input" aria-describedby="description" aria-invalid="false" aria-label="Enter a search string to filter the list of notebooks shown below." type="text">
        <!--?lit$040125974$-->
      </div>
    
      <!--?lit$040125974$-->
      <span class="icon trailing" slot="end">
        <slot name="trailing-icon"></slot>
      </span>
    
      <div id="description" slot="aria-describedby"></div>
      <slot name="container" slot="container"></slot>
    </md-outlined-field>
      </span>
    </template>
          <md-icon slot="trailing-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>search</md-icon>
        </md-outlined-text-field>
        <div>
          <slot name="reload"></slot>
          <slot name="clearhistory"></slot>
        </div>
      </section>
      <div class="dialog-table" role="table" aria-label="Example notebooks">
        <div role="rowgroup">
          <div role="row" class="dialog-table-header  wide-cols">
            <span class="icon-column" role="columnheader" aria-label="Icon"></span>
            <span class="title-column" role="columnheader"><!--?lit$040125974$-->Title</span>
            <!--?lit$040125974$-->
            <!--?lit$040125974$-->
            <!--?lit$040125974$-->
            <span class="grow"></span>
            <span class="screenreader-only" role="columnheader"><!--?lit$040125974$-->Actions</span>
          </div>
        </div>
        <!--?lit$040125974$--><div id="num-results" aria-atomic="true" class="screenreader-only" aria-live="polite">
        <!--?lit$040125974$-->20 results
      </div>
      <mwc-list innerrole="rowgroup" itemroles="row" style="display: block; position: relative; contain: size layout; overflow: auto; min-height: 150px;"><template shadowrootmode="open"><!---->
      <!-- @ts-ignore -->
      <ul class="mdc-deprecated-list" tabindex="-1" role="rowgroup">
        <slot></slot>
        <!--?lit$040125974$-->
      </ul>
    </template>
        <!--?lit$040125974$--><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="0" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 0px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <mwc-ripple><template shadowrootmode="open"><!---->
        <div class="mdc-ripple-surface mdc-ripple-upgraded"></div></template>
      </mwc-ripple>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/basic_features_overview.ipynb" title="Overview of Colab Features">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Overview of Colab Features</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/basic_features_overview.ipynb" title="Open &quot;Overview of Colab Features&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 64px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <mwc-ripple><template shadowrootmode="open"><!---->
        <div class="mdc-ripple-surface mdc-ripple-upgraded"></div></template>
      </mwc-ripple>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/markdown_guide.ipynb" title="Markdown Guide">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Markdown Guide</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/markdown_guide.ipynb" title="Open &quot;Markdown Guide&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 128px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/charts.ipynb" title="Charts in Colab">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Charts in Colab</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/charts.ipynb" title="Open &quot;Charts in Colab&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 192px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/io.ipynb" title="External data: Drive, Sheets, and Cloud Storage">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->External data: Drive, Sheets, and Cloud Storage</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/io.ipynb" title="Open &quot;External data: Drive, Sheets, and Cloud Storage&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 256px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <mwc-ripple><template shadowrootmode="open"><!---->
        <div class="mdc-ripple-surface mdc-ripple-upgraded"></div></template>
      </mwc-ripple>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/bigquery.ipynb" title="Getting started with BigQuery">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Getting started with BigQuery</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/bigquery.ipynb" title="Open &quot;Getting started with BigQuery&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 320px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/forms.ipynb" title="Forms">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Forms</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/forms.ipynb" title="Open &quot;Forms&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 384px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/data_table.ipynb" title="Data Table">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Data Table</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/data_table.ipynb" title="Open &quot;Data Table&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 448px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/accessing_files.ipynb" title="Accessing Files">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Accessing Files</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/accessing_files.ipynb" title="Open &quot;Accessing Files&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 512px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/advanced_outputs.ipynb" title="Advanced Outputs Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Advanced Outputs Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/advanced_outputs.ipynb" title="Open &quot;Advanced Outputs Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 576px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/altair.ipynb" title="Altair Chart Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Altair Chart Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/altair.ipynb" title="Open &quot;Altair Chart Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 640px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/bigquery.ipynb" title="BigQuery Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->BigQuery Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/bigquery.ipynb" title="Open &quot;BigQuery Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 704px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/gemini.ipynb" title="Gemini Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Gemini Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/gemini.ipynb" title="Open &quot;Gemini Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 768px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/drive.ipynb" title="Google Drive Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Google Drive Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/drive.ipynb" title="Open &quot;Google Drive Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 832px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/gcs.ipynb" title="Google Cloud Storage Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Google Cloud Storage Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/gcs.ipynb" title="Open &quot;Google Cloud Storage Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" tabindex="-1" role="row" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 896px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/gcp_auth.ipynb" title="GCP Authentication">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->GCP Authentication</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/gcp_auth.ipynb" title="Open &quot;GCP Authentication&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 960px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/forms.ipynb" title="Forms Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Forms Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/forms.ipynb" title="Open &quot;Forms Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 1024px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb" title="Library Import Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Library Import Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb" title="Open &quot;Library Import Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 1088px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/pandas.ipynb" title="Pandas Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Pandas Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/pandas.ipynb" title="Open &quot;Pandas Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 1152px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/sheets.ipynb" title="Google Sheets Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Google Sheets Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/sheets.ipynb" title="Open &quot;Google Sheets Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!----><!----><mwc-list-item twoline="" graphic="icon" mwc-list-item="" role="row" tabindex="-1" aria-disabled="false" aria-selected="false" style="position: absolute; box-sizing: border-box; transform: translate(0px, 1216px); top: 0px;"><template shadowrootmode="open"><!---->
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__graphic material-icons   ">
        <slot name="graphic"></slot>
      </span>
      <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__text">
        <!--?lit$040125974$-->
      <span class="mdc-deprecated-list-item__primary-text">
        <slot></slot>
      </span>
      <span class="mdc-deprecated-list-item__secondary-text">
        <slot name="secondary"></slot>
      </span>
    
      </span>
      <!--?lit$040125974$--><!--?--><!--?--></template>
      <md-icon slot="graphic" role="cell" title="Example notebook"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      <div class="item-row   wide-cols">
        <div class="title-column multiline-column" role="cell">
          <a class="row-link" href="https://colab.research.google.com/notebooks/snippets/earth_engine.ipynb" title="Earth Engine Snippets">
            <div class="row-link-text nowrap multiline-primary"><!--?lit$040125974$-->Earth Engine Snippets</div>
          </a>
          <div class="secondary"><!--?lit$040125974$--><!--?lit$040125974$--></div>
        </div>
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <!--?lit$040125974$-->
        <div class="grow"></div>
        <div class="small-icon-action-column" role="cell">
          <div class="small-icon-action">
            <!--?lit$040125974$-->
          </div>
          <div class="small-icon-action">
            <a target="_blank" href="https://colab.research.google.com/notebooks/snippets/earth_engine.ipynb" title="Open &quot;Earth Engine Snippets&quot; in new tab">
              <md-icon class="small-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>open_in_new</md-icon>
            </a>
          </div>
        </div>
      </div>
    </mwc-list-item><!---->
      <div virtualizer-sizer="" style="position: absolute; margin: -2px 0px 0px; padding: 0px; visibility: hidden; font-size: 2px; transform: translate(0px, 1280px);">&amp;nbsp;</div></mwc-list>
      </div>
    </div></template></colab-notebook-list><!--?--><!--?--></div><!----><!----><div class="pagecontent right-content" slot="page-1">
      <!----><!--?lit$040125974$--><!--?lit$040125974$--><colab-notebook-list><template shadowrootmode="open"><!----> <div class="dialog-table-container">
      <section class="dialog-table-input-row">
        <md-outlined-text-field id="dialog-table-filter-input" label="Search notebooks" data-aria-label="Enter a search string to filter the list of notebooks shown below." inputmode="" type="text" autocomplete=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <span class="text-field   ">
        <!--?lit$040125974$--><md-outlined-field class="field" count="0" error-text="" label="Search notebooks" max="-1" supporting-text="" has-end=""><template shadowrootmode="open"><!---->
      <div class="field with-end">
        <div class="container-overflow">
          <!--?lit$040125974$-->
          <slot name="container"></slot>
          <!--?lit$040125974$--> <!--?lit$040125974$--> <!--?lit$040125974$-->
      <div class="outline">
        <div class="outline-start"></div>
        <div class="outline-notch">
          <div class="outline-panel-inactive"></div>
          <div class="outline-panel-active"></div>
          <div class="outline-label"><!--?lit$040125974$-->
      <span class="label  hidden floating " aria-hidden="true"><!--?lit$040125974$-->Search notebooks</span>
    </div>
        </div>
        <div class="outline-end"></div>
      </div>
    
          <div class="container">
            <div class="start">
              <slot name="start"></slot>
            </div>
            <div class="middle">
              <div class="label-wrapper">
                <!--?lit$040125974$-->
      <span class="label  resting " aria-hidden="false"><!--?lit$040125974$-->Search notebooks</span>
     <!--?lit$040125974$-->
              </div>
              <div class="content">
                <slot></slot>
              </div>
            </div>
            <div class="end">
              <slot name="end"></slot>
            </div>
          </div>
        </div>
        <!--?lit$040125974$-->
      </div>
    </template>
      <!--?lit$040125974$-->
      <span class="icon leading" slot="start">
        <slot name="leading-icon"></slot>
      </span>
    
      <!--?lit$040125974$-->
      <div class="input-wrapper">
        <!--?lit$040125974$-->
        <input class="input" aria-describedby="description" aria-invalid="false" aria-label="Enter a search string to filter the list of notebooks shown below." type="text">
        <!--?lit$040125974$-->
      </div>
    
      <!--?lit$040125974$-->
      <span class="icon trailing" slot="end">
        <slot name="trailing-icon"></slot>
      </span>
    
      <div id="description" slot="aria-describedby"></div>
      <slot name="container" slot="container"></slot>
    </md-outlined-field>
      </span>
    </template>
          <md-icon slot="trailing-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>search</md-icon>
        </md-outlined-text-field>
        <div>
          <slot name="reload"></slot>
          <slot name="clearhistory"></slot>
        </div>
      </section>
      <div class="dialog-table" role="table" aria-label="Recent notebooks">
        <div role="rowgroup">
          <div role="row" class="dialog-table-header  ">
            <span class="icon-column" role="columnheader" aria-label="Icon"></span>
            <span class="title-column" role="columnheader"><!--?lit$040125974$-->Title</span>
            <!--?lit$040125974$-->
            <!--?lit$040125974$--><span role="columnheader" class="date-column date-column-last clickable" aria-sort="descending">
                  <button class="sort" title="Sort by when notebook was last accessed">
                    <!--?lit$040125974$-->Last opened
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->arrow_downward_alt</md-icon>
                  </button>
                </span>
            <!--?lit$040125974$--><span role="columnheader" class="date-column date-column-first clickable">
                  <button class="sort" title="Sort by when notebook was first opened">
                    <!--?lit$040125974$-->First opened
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->swap_vert</md-icon>
                  </button>
                </span>
            <span class="grow"></span>
            <span class="screenreader-only" role="columnheader"><!--?lit$040125974$-->Actions</span>
          </div>
        </div>
        <!--?lit$040125974$--><div id="num-results" aria-atomic="true" class="screenreader-only" aria-live="polite">
        <!--?lit$040125974$-->1 result
      </div>
      <mwc-list innerrole="rowgroup" itemroles="row" style="display: block; position: relative; contain: size layout; overflow: auto; min-height: 150px;"><template shadowrootmode="open"><!---->
      <!-- @ts-ignore -->
      <ul class="mdc-deprecated-list" tabindex="-1" role="rowgroup">
        <slot></slot>
        <!--?lit$040125974$-->
      </ul>
    </template>
        <!--?lit$040125974$-->
      <div virtualizer-sizer="" style="position: absolute; margin: -2px 0px 0px; padding: 0px; visibility: hidden; font-size: 2px; transform: translate(0px, 64px);">&amp;nbsp;</div></mwc-list>
      </div>
    </div></template><md-icon-button slot="clearhistory" class="colab-icon clear-history" data-aria-label="Clear history" title="Clear history" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Clear history">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>delete</md-icon>
      </md-icon-button></colab-notebook-list><!--?--><!--?--></div><!----><!----><div class="pagecontent right-content" slot="page-2">
      </div><!----><!----><div class="pagecontent right-content" slot="page-3">
      </div><!----><!----><div class="pagecontent right-content" slot="page-4">
      </div><!---->
      </colab-pages>
    </colab-side-tab-dialog-page-viewer>
  </div><!----><!----><!----> <md-filled-button slot="secondaryAction" class="new-notebook" dialogaction="create" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$040125974$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$040125974$--><button id="button" class="button">
      <!--?lit$040125974$-->
      <span class="touch"></span>
      <!--?lit$040125974$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$040125974$-->
    
    </button>
    </template>
    <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
    <!--?lit$040125974$-->New notebook
  </md-filled-button><!----><!----> <md-text-button slot="primaryAction" class="dismiss" dialogaction="cancel" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$040125974$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$040125974$--><button id="button" class="button">
      <!--?lit$040125974$-->
      <span class="touch"></span>
      <!--?lit$040125974$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$040125974$-->
    
    </button>
    </template>
    <!--?lit$040125974$-->Cancel
  </md-text-button><!----><!----></mwc-dialog><div class="notebook-vertical colab-left-pane-open" inert="" aria-hidden="true" style="position: relative;">
      <div class="top-floater"><div role="banner">
    <colab-header-skip-button><template shadowrootmode="open"><!----><a id="skiplink" class="skip-link" href="https://colab.research.google.com/#top-toolbar" tabindex="-1"><!--?lit$040125974$-->Skip to main content</a></template></colab-header-skip-button>
    <!--?lit$040125974$-->
    <!--?lit$040125974$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning hidden">
            <!--?lit$040125974$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip" tabindex="-1">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
          <mwc-icon-button class="close" icon="close" title="Close"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Close" tabindex="-1"><!--?lit$040125974$-->
    <!--?lit$040125974$--><i class="material-icons"><!--?lit$040125974$-->close</i>
    <span><slot></slot></span>
  </button></template></mwc-icon-button></div>
        
    <!--?lit$040125974$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><div id="header-logo">
              <!--?lit$040125974$--> <!--?lit$040125974$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive" tabindex="-1">
        <!--?lit$040125974$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$040125974$--> <!--?lit$040125974$-->
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" disabled="" fdprocessedid="q59oam" style="width: 158.156px;"><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">Welcome To Colab_</colab-input-sizer>
            <!--?lit$040125974$-->
            <!--?lit$040125974$-->
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" style="user-select: none;"><!--?lit$040125974$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$040125974$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$040125974$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$040125974$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$040125974$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$040125974$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$040125974$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$040125974$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div>
    <div id="colab-menu-cover" style="display: none;"> </div></div><!----><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><!--?--></template></colab-last-saved-indicator></div></div>
        <div id="header-right">
          <!--?lit$040125974$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$040125974$-->
      <!--?lit$040125974$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$040125974$-->
          <!--?lit$040125974$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$040125974$--> <md-text-button id="share-toolbar-button" command="share" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$040125974$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$040125974$--><button id="button" class="button" tabindex="-1">
      <!--?lit$040125974$-->
      <span class="touch"></span>
      <!--?lit$040125974$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$040125974$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->link</md-icon>
                <!--?lit$040125974$-->Share
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Ea gb_Id gb_2d gb_Vc" id="gb"><div class="gb_Bd gb_Zd gb_wd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Re" style="display:block"><div class="gb_2c"></div><div class="gb_y gb_bd gb_Nf gb_Z"><div class="gb_C gb_ib gb_Nf gb_Z"><a class="gb_A gb_Xa gb_Z" aria-expanded="false" aria-label="Google Account: madani roshan  
(sunnyrockzzmadani@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en&amp;continue=https://colab.research.google.com/&amp;ec=GBRAqQM" tabindex="-1" role="button"><img class="gb_O gbii" src="./python_files/unnamed.jpg" srcset="https://lh3.googleusercontent.com/ogw/AF2bZyhnHkjD5WskIlwRMYDn87xiOCDfN0A3J8Z0RIau3ylApdY=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AF2bZyhnHkjD5WskIlwRMYDn87xiOCDfN0A3J8Z0RIau3ylApdY=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""><div class="gb_P gb_Q" aria-hidden="true"><svg class="gb_Ja" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_Ka" cx="7" cy="7" r="7"></circle><path class="gb_Ma" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.xd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.xd(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("B`"+b))}};
}catch(e){_._DumpException(e)}
try{
var yd=document.querySelector(".gb_I .gb_A"),zd=document.querySelector("#gb.gb_Rc");yd&&!zd&&_.xd(_.gd,yd,"click");
}catch(e){_._DumpException(e)}
try{
_.ch=function(a){const b=[];let c=0;for(const d in a)b[c++]=a[d];return b};_.dh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].ma()&&a.i[b].B())return a.i[b];return null};_.eh=function(a,b){a.i[b.K()]=b};var fh=new class extends _.R{constructor(){var a=_.Qc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.dh(this)&&_.dh(this).K()==a||this.i[a].R(!0))}Ra(a){this.j=a;for(const b in this.i)this.i[b].ma()&&this.i[b].Ra(a)}hc(a){return a in this.i?this.i[a]:null}};_.jd("dd",fh);
}catch(e){_._DumpException(e)}
try{
_.wi=function(a,b){return _.M(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var xi=document.querySelector(".gb_y .gb_A"),yi=document.querySelector("#gb.gb_Rc");xi&&!yi&&_.xd(_.gd,xi,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><div class="notebook-horizontal">
        <!--?lit$040125974$--><colab-left-pane role="complementary" aria-label="left pane" class="colab-left-pane-open"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$040125974$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" selected="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  selected standard " aria-label="Table of contents" aria-pressed="true" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="icon icon--selected"><slot name="selected"><slot></slot></slot></span>
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$040125974$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$040125974$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->search</md-icon>
    </md-icon-button> <!--?lit$040125974$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$040125974$--><md-icon-button toggle="" command="show-variables" data-aria-label="Variables" title="Variables" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Variables" aria-pressed="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <path d="M4.51,9.44V6.08c0-1.34.37-1.85,1.6-2.17l.22-.06V3.13l-.27,0-.44,0a4.46,4.46,0,0,0-2.2.59,2.78,2.78,0,0,0-1,2.51V9.74c0,1.26-.26,1.61-1.49,2L0,12l.94.29c1.21.38,1.49.75,1.49,2v3.5a2.94,2.94,0,0,0,1,2.6,4.39,4.39,0,0,0,2.14.56l.46,0,.27,0v-.72l-.22-.06c-1.24-.32-1.6-.81-1.6-2.17V14.58c0-1.43-.3-2.13-1.25-2.57C4.2,11.57,4.51,10.87,4.51,9.44Z"></path>
      <path d="M23.06,11.71c-1.22-.36-1.49-.71-1.49-2l0-3.5a3,3,0,0,0-1-2.6,4.38,4.38,0,0,0-2.14-.56l-.46,0-.27,0v.72l.22.06c1.24.32,1.6.81,1.6,2.17V9.44c0,1.44.3,2.13,1.25,2.57-1,.44-1.25,1.14-1.25,2.57v3.36c0,1.34-.37,1.85-1.6,2.17l-.22.06v.72l.27,0,.44,0a4.47,4.47,0,0,0,2.2-.59,2.82,2.82,0,0,0,1-2.51V14.28c0-1.26.26-1.61,1.49-2L24,12Z"></path>
      <path d="M15.16,8.22a.88.88,0,0,1,.46.16,1.25,1.25,0,0,0,.69.2h0A1,1,0,0,0,17,8.23a1.06,1.06,0,0,0,.24-.8,1.1,1.1,0,0,0-1.15-1h0c-1,0-1.73.64-3,2.57l-.12-.51c-.28-1.36-.56-2-1.39-2h0A8,8,0,0,0,9,7.08l-.47.16.16.91L9.41,8a3.22,3.22,0,0,1,.73-.14c.34,0,.43,0,.71,1.2l.56,2.47L9.76,13.82a3.6,3.6,0,0,1-.8.88.9.9,0,0,1-.38-.13,1.83,1.83,0,0,0-.88-.28,1,1,0,0,0-1,1.06A1.15,1.15,0,0,0,8,16.53c.85,0,1.35-.35,2.24-1.55l1.49-2,.46,1.88c.23,1,.46,1.66,1.53,1.66s1.66-.75,2.81-2.53l.17-.26-.81-.48-.16.2-.25.34-.19.25c-.45.57-.62.73-.76.73s-.28-.4-.34-.63l-.67-2.83a4.2,4.2,0,0,1-.15-.79C13.84,9.78,14.74,8.22,15.16,8.22Z"></path></svg></md-icon>
    </md-icon-button> <!--?lit$040125974$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$040125974$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$040125974$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$040125974$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->folder</md-icon>
    </md-icon-button> <!--?lit$040125974$-->
      </div></div>
        <div class="left-pane-bottom"><!----><div class="left-pane-button">
        <!--?lit$040125974$--><md-icon-button command="snippets" data-aria-label="Code snippets" title="Code snippets" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->code</md-icon>
    </md-icon-button> <!--?lit$040125974$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$040125974$--><md-icon-button command="show-command-palette" data-aria-label="Command palette" title="Command palette" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Command palette" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$-->
      <path d="M21,3H3A2,2,0,0,0,1,5V17a2,2,0,0,0,2,2H21a2,2,0,0,0,2-2V5A2,2,0,0,0,21,3Zm0,2V17H3V5"></path>
      <rect x="5" y="12" width="11" height="2"></rect>
      <rect x="5" y="8" width="11" height="2"></rect>
      <rect x="17" y="8" width="2" height="2"></rect>
      <rect x="17" y="12" width="2" height="2"></rect></svg></md-icon>
    </md-icon-button> <!--?lit$040125974$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$040125974$--><md-icon-button command="show-terminal" data-aria-label="Terminal" title="Terminal" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Terminal" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->terminal</md-icon>
    </md-icon-button> <!--?lit$040125974$-->
      </div></div>
      </div><colab-resizer class="ew-resize">
          <div class="resizer-contents">
            <div class="colab-left-pane-header layout horizontal noshrink">
              <h3 class="left-pane-content-title">Table of contents</h3>
              <!--?lit$040125974$--><md-icon-button class="colab-left-pane-move" data-aria-label="Move left pane to a tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move left pane to a tab" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>tab</md-icon>
    </md-icon-button> <!--?lit$040125974$--><md-icon-button class="colab-left-pane-close" data-aria-label="Close left pane" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close left pane" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
    </md-icon-button>
            </div>
            <div class="left-pane-container"><colab-table-of-contents class="layout vertical"><!----> <colab-shaded-scroller shade-bottom="" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 4px -7px inset, rgba(0, 0, 0, 0.15) 0px -4px 4px -7px inset;">
        <div class="colab-toc-sections"> <div>
      <div class="toc-cell"><!--?lit$040125974$--> <a href="https://colab.research.google.com/#scrollTo=Getting_started" tabindex="-1">
      <!--?lit$040125974$--><span><span>Getting started</span></span>

    </a> <!--?lit$040125974$--><md-icon-button data-aria-label="Open menu for Getting started" title="Open menu for Getting started" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open menu for Getting started" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
        </md-icon-button></div>
      <!--?lit$040125974$--><div class="toc-section-cells"></div>
    </div><div>
      <div class="toc-cell"><!--?lit$040125974$--> <a href="https://colab.research.google.com/#scrollTo=Data_science" tabindex="-1">
      <!--?lit$040125974$--><span>Data science</span>

    </a> <!--?lit$040125974$--><md-icon-button data-aria-label="Open menu for Data science" title="Open menu for Data science" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open menu for Data science" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
        </md-icon-button></div>
      <!--?lit$040125974$--><div class="toc-section-cells"></div>
    </div><div>
      <div class="toc-cell"><!--?lit$040125974$--> <a href="https://colab.research.google.com/#scrollTo=Machine_learning" tabindex="-1">
      <!--?lit$040125974$--><span>Machine learning</span>

    </a> <!--?lit$040125974$--><md-icon-button data-aria-label="Open menu for Machine learning" title="Open menu for Machine learning" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open menu for Machine learning" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
        </md-icon-button></div>
      <!--?lit$040125974$--><div class="toc-section-cells"></div>
    </div><div>
      <div class="toc-cell"><!--?lit$040125974$--> <a href="https://colab.research.google.com/#scrollTo=More_Resources" tabindex="-1">
      <!--?lit$040125974$--><span>More Resources</span>

    </a> <!--?lit$040125974$--><md-icon-button data-aria-label="Open menu for More Resources" title="Open menu for More Resources" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open menu for More Resources" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
        </md-icon-button></div>
      <!--?lit$040125974$--><div class="toc-section-cells"><div>
      <div class="toc-cell"><!--?lit$040125974$--> <a href="https://colab.research.google.com/#scrollTo=Featured_examples" tabindex="-1">
      <!--?lit$040125974$--><span>Featured examples</span>

    </a> <!--?lit$040125974$--><md-icon-button data-aria-label="Open menu for Featured examples" title="Open menu for Featured examples" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open menu for Featured examples" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
        </md-icon-button></div>
      <!--?lit$040125974$-->
    </div></div>
    </div></div>
        <!--?lit$040125974$--> <md-outlined-button class="toc-add-section" data-aria-label="Add section" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$040125974$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$040125974$--><button id="button" class="button" aria-label="Add section" tabindex="-1">
      <!--?lit$040125974$-->
      <span class="touch"></span>
      <!--?lit$040125974$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$040125974$-->
    
    </button>
    </template>
              <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
              <!--?lit$040125974$-->Section
            </md-outlined-button>
      </colab-shaded-scroller></colab-table-of-contents></div>
          </div>
        <div class="resizer-thumb"></div></colab-resizer></colab-left-pane>
        <div class="layout vertical grow">
          <colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$040125974$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$040125974$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$040125974$--><button id="button" class="button" tabindex="-1">
      <!--?lit$040125974$-->
      <span class="touch"></span>
      <!--?lit$040125974$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$040125974$-->
    
    </button>
    </template>
        <!--?lit$040125974$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$040125974$--><span class="screenreader-only"><!--?lit$040125974$-->Insert code cell below <!--?lit$040125974$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$040125974$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$040125974$-->Code
          </colab-toolbar-button>
          <!--?lit$040125974$-->
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$040125974$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$040125974$--><button id="button" class="button" tabindex="-1">
      <!--?lit$040125974$-->
      <span class="touch"></span>
      <!--?lit$040125974$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$040125974$-->
    
    </button>
    </template>
        <!--?lit$040125974$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$040125974$--><span class="screenreader-only"><!--?lit$040125974$-->Add text cell <!--?lit$040125974$--></span>
      </md-text-button>
      <!--?lit$040125974$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$040125974$-->Text
          </colab-toolbar-button>
        
    <!--?lit$040125974$-->
    <!--?lit$040125974$--> <span class="expanded-options">
          <span class="colab-separator"></span>
          <colab-toolbar-button command="clone"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$040125974$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$040125974$--><button id="button" class="button" tabindex="-1">
      <!--?lit$040125974$-->
      <span class="touch"></span>
      <!--?lit$040125974$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$040125974$-->
    
    </button>
    </template>
        <!--?lit$040125974$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$040125974$--><span class="screenreader-only"><!--?lit$040125974$--> <!--?lit$040125974$--></span>
      </md-text-button>
      <!--?lit$040125974$--><!--?--></template>
            <!--?lit$040125974$-->Copy to Drive
          </colab-toolbar-button>
        </span>
    <!--?lit$040125974$-->
    <!--?lit$040125974$-->
    <!--?lit$040125974$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><!--?--></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$040125974$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$040125974$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$040125974$--><!--?lit$040125974$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$040125974$--><!--?-->
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Connect to a new runtime"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$040125974$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$040125974$--><button id="button" class="button" tabindex="-1">
      <!--?lit$040125974$-->
      <span class="touch"></span>
      <!--?lit$040125974$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$040125974$-->
    
    </button>
    </template>
        <!--?lit$040125974$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$040125974$--><span class="screenreader-only"><!--?lit$040125974$-->Connect to a new runtime <!--?lit$040125974$--></span>
      </md-text-button>
      <!--?lit$040125974$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connect to a new runtime" shortcut=""><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Connect to a new runtime</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$040125974$-->Connect
      </colab-toolbar-button>
      <!--?lit$040125974$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$040125974$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$040125974$--> <span class="colab-separator"></span>
          <colab-toolbar-button command="show-chat" icon="spark"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$040125974$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$040125974$--><button id="button" class="button" tabindex="-1">
      <!--?lit$040125974$-->
      <span class="touch"></span>
      <!--?lit$040125974$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$040125974$-->
    
    </button>
    </template>
        <!--?lit$040125974$-->
    <svg slot="icon" viewBox="0 -960 960 960" width="24" height="24">
      <defs>
        <lineargradient id="sparkGradient" x1="0" y1="1" x2="1" y2="0">
          <stop offset="33.06%" stop-color="#217BFE"></stop>
          <stop offset="44.4%" stop-color="#078EFB"></stop>
          <stop offset="65.69%" stop-color="#A190FF"></stop>
          <stop offset="75.05%" stop-color="#BD99FE"></stop>
        </lineargradient>
      </defs>
      <path fill="url(#sparkGradient)" d="M480-80q2 0 2-2 0-82 31-154t85-126q54-54 126-85t154-31q2 0 2-2t-2-2q-82 0-154-31t-126-85q-54-54-85-126t-31-154q0-2-2-2t-2 2q0 82-31 154t-85 126q-54 54-126 85T82-482q-2 0-2 2t2 2q82 0 154 31t126 85q54 54 85 126t31 154q0 2 2 2Z"></path>
    </svg>
        <span class="button-content"><slot></slot></span>
        <!--?lit$040125974$--><span class="screenreader-only"><!--?lit$040125974$--> <!--?lit$040125974$--></span>
      </md-text-button>
      <!--?lit$040125974$--><!--?--></template>
            <!--?lit$040125974$-->Gemini
          </colab-toolbar-button>
    <!--?lit$040125974$-->
    <span class="collapsed-options">
      <!--?lit$040125974$--><span class="colab-separator"></span>
      <!--?lit$040125974$--> <md-icon-button command="share" title="Share notebook" data-aria-label="Share notebook" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->link</md-icon>
          </md-icon-button><md-icon-button command="preferences" data-aria-label="Open settings" title="Open settings" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$040125974$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$040125974$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$040125974$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-gw_AH0J_ezcS" class="selected-tab" md-tab="" active="" tabindex="0"><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$040125974$--><div class="indicator"></div>
      </div>
      <!--?lit$040125974$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-gw_AH0J_ezcS"><!--?lit$040125974$--><!--?lit$040125974$-->Notebook<!--?--></span>
            <!--?lit$040125974$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$040125974$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" role="main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$040125974$-->
              <div class="notebook-content ">
                <!--?lit$040125974$--><div class="add-cell">
      <hr>
    </div>
                <div class="notebook-cell-list"><div class="cell text" id="cell-Wf5KrEb6vrkR" role="region" aria-label="Cell 0: Text cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="markdown-google-sans">
  <div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 0 child cells under  (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 0 child cells under  (Press &lt;Shift&gt; to also collapse sibling sections)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 0 child cells under  (Press &lt;Shift&gt; to also collapse sibling sections)" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1>Welcome to Colab!</h1></div>
</div>

<div class="markdown-google-sans">
  <h2>Explore the Gemini API</h2>
  <p>The Gemini API gives you access to Gemini models created by Google DeepMind. Gemini models are built from the ground up to be multimodal, so you can reason seamlessly across text, images, code, and audio.
  </p>
  <strong>How to get started</strong>
    <ol>
      <li>Go to <a href="https://www.google.com/url?q=https%3A%2F%2Faistudio.google.com%2F" target="_blank" rel="nofollow" aria-label="Google AI Studio Link will open in a new tab" tabindex="-1">Google AI Studio</a> and log in with your Google account.</li>
      <li><a href="https://www.google.com/url?q=https%3A%2F%2Faistudio.google.com%2Fapp%2Fapikey" target="_blank" rel="nofollow" aria-label="Create an API key Link will open in a new tab" tabindex="-1">Create an API key</a>.</li>
      <li>Use a quickstart for <a href="https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Prompting.ipynb" target="_blank" rel="nofollow" aria-label="Python Link will open in a new tab" tabindex="-1">Python</a>, or call the REST API using <a href="https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/rest/Prompting_REST.ipynb" target="_blank" rel="nofollow" aria-label="curl Link will open in a new tab" tabindex="-1">curl</a>.</li>
      </ol>
  <strong>Explore use cases</strong>
    <ul>
      <li><a href="https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Market_a_Jet_Backpack.ipynb" target="_blank" rel="nofollow" aria-label="Create a marketing campaign Link will open in a new tab" tabindex="-1">Create a marketing campaign</a></li>
      <li><a href="https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Audio.ipynb" target="_blank" rel="nofollow" aria-label="Analyze audio recordings Link will open in a new tab" tabindex="-1">Analyze audio recordings</a></li>
      <li><a href="https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/System_instructions.ipynb" target="_blank" rel="nofollow" aria-label="Use System instructions in chat Link will open in a new tab" tabindex="-1">Use System instructions in chat</a></li>
    </ul>
  <p>To learn more, check out the <a href="https://github.com/google-gemini/cookbook" target="_blank" rel="nofollow" aria-label="Gemini cookbook Link will open in a new tab" tabindex="-1">Gemini cookbook</a> or visit the <a href="https://www.google.com/url?q=https%3A%2F%2Fai.google.dev%2Fdocs%2F" target="_blank" rel="nofollow" aria-label="Gemini API documentation Link will open in a new tab" tabindex="-1">Gemini API documentation</a>.
  </p>
</div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-Nma_JWh-W-IF" role="region" aria-label="Cell 1: Text cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p><span>Colab now has AI features powered by <a href="https://www.google.com/url?q=https%3A%2F%2Fgemini.google.com" target="_blank" rel="nofollow" aria-label="Gemini Link will open in a new tab" tabindex="-1">Gemini</a>. The video below provides information on how to use these features, whether you're new to Python, or a seasoned veteran.</span></p>
<center>
  <a href="https://www.youtube.com/watch?v=V7RXyqFUR98" target="_blank" rel="nofollow" aria-label="
  
   Link will open in a new tab" tabindex="-1">
  <img alt="Thumbnail for a video showing 3 AI-powered Google Colab features" src="data:image/png;base64,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" height="188" width="336">
  </a>
</center></span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code icon-scrolling" id="cell-zwFnJsE6vjf8" role="region" aria-label="Cell 2: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$040125974$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark" data-lang="notebook-python"><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: block;"><template shadowrootmode="open"><!----><div><!--?lit$040125974$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 2 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-5fCEDCU_qrC0" role="region" aria-label="Cell 3: Text cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="markdown-google-sans">
  <div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 0 child cells under  (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 0 child cells under  (Press &lt;Shift&gt; to also collapse sibling sections)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 0 child cells under  (Press &lt;Shift&gt; to also collapse sibling sections)" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h2>What is Colab?</h2></div>
</div>

<p>Colab, or "Colaboratory", allows you to write and execute Python in your browser, with </p>
<ul>
<li>Zero configuration required</li>
<li>Access to GPUs free of charge</li>
<li>Easy sharing</li>
</ul>
<p>Whether you're a <strong>student</strong>, a <strong>data scientist</strong> or an <strong>AI researcher</strong>, Colab can make your work easier. Watch <a href="https://www.youtube.com/watch?v=inN8seMm7UI" target="_blank" rel="nofollow" aria-label="Introduction to Colab Link will open in a new tab" tabindex="-1">Introduction to Colab</a> or <a href="https://www.youtube.com/watch?v=rNgswRZ2C1Y" target="_blank" rel="nofollow" aria-label="Colab Features You May Have Missed Link will open in a new tab" tabindex="-1">Colab Features You May Have Missed</a> to learn more, or just get started below!</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-GJBs_flRovLc" role="region" aria-label="Cell 4: Text cell: Getting started" style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="markdown-google-sans">

<div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 4 child cells under Getting started (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 4 child cells under Getting started (Press &lt;Shift&gt; to also collapse sibling sections)" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 4 child cells under Getting started (Press &lt;Shift&gt; to also collapse sibling sections)" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h2><strong>Getting started</strong></h2></div>
</div>

<p>The document you are reading is not a static web page, but an interactive environment called a <strong>Colab notebook</strong> that lets you write and execute code.</p>
<p>For example, here is a <strong>code cell</strong> with a short Python script that computes a value, stores it in a variable, and prints the result:</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 4 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output icon-scrolling" id="cell-gJr_9dXGpJ05" role="region" aria-label="Cell 5: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$040125974$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$040125974$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk1">seconds_in_a_day&nbsp;=&nbsp;</span><span class="mtk6">24</span><span class="mtk1">&nbsp;*&nbsp;</span><span class="mtk6">60</span><span class="mtk1">&nbsp;*&nbsp;</span><span class="mtk6">60</span></span><br><span><span class="mtk1">seconds_in_a_day</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$040125974$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 5 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$040125974$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="execute_result output_text"><pre>86400</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-2fhs6GZ4qFMx" role="region" aria-label="Cell 6: Text cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p>To execute the code in the above cell, select it with a click and then either press the play button to the left of the code, or use the keyboard shortcut "Command/Ctrl+Enter". To edit the code, just click the cell and start editing.</p>
<p>Variables that you define in one cell can later be used in other cells:</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output icon-scrolling" id="cell--gE-Ez1qtyIA" role="region" aria-label="Cell 7: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$040125974$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$040125974$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk1">seconds_in_a_week&nbsp;=&nbsp;</span><span class="mtk6">7</span><span class="mtk1">&nbsp;*&nbsp;seconds_in_a_day</span></span><br><span><span class="mtk1">seconds_in_a_week</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$040125974$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 7 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$040125974$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer role="group"><div><div class="execute_result output_text"><pre>604800</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-lSrWNr3MuFUS" role="region" aria-label="Cell 8: Text cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p>Colab notebooks allow you to combine <strong>executable code</strong> and <strong>rich text</strong> in a single document, along with <strong>images</strong>, <strong>HTML</strong>, <strong>LaTeX</strong> and more. When you create your own Colab notebooks, they are stored in your Google Drive account. You can easily share your Colab notebooks with co-workers or friends, allowing them to comment on your notebooks or even edit them. To learn more, see <a href="https://colab.research.google.com/notebooks/basic_features_overview.ipynb" target="_blank" rel="nofollow" aria-label="Overview of Colab Link will open in a new tab" tabindex="-1">Overview of Colab</a>. To create a new Colab notebook you can use the File menu above, or use the following link: <a href="http://colab.research.google.com/#create=true" target="_blank" rel="nofollow" aria-label="create a new Colab notebook Link will open in a new tab" tabindex="-1">create a new Colab notebook</a>.</p>
<p>Colab notebooks are Jupyter notebooks that are hosted by Colab. To learn more about the Jupyter project, see <a href="https://www.jupyter.org/" target="_blank" rel="nofollow" aria-label="jupyter.org Link will open in a new tab" tabindex="-1">jupyter.org</a>.</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-UdRyKR44dcNI" role="region" aria-label="Cell 9: Text cell: Data science" style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="markdown-google-sans">

<div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 4 child cells under Data science (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 4 child cells under Data science (Press &lt;Shift&gt; to also collapse sibling sections)" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 4 child cells under Data science (Press &lt;Shift&gt; to also collapse sibling sections)" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h2>Data science</h2></div>
</div>

<p>With Colab you can harness the full power of popular Python libraries to analyze and visualize data. The code cell below uses <strong>numpy</strong> to generate some random data, and uses <strong>matplotlib</strong> to visualize it. To edit the code, just click the cell and start editing.</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 4 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-4_kCnsPUqS6o" role="region" aria-label="Cell 10: Text cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p>You can import your own data into Colab notebooks from your Google Drive account, including from spreadsheets, as well as from Github and many other sources. To learn more about importing data, and how Colab can be used for data science, see the links below under <a href="https://colab.research.google.com/#working-with-data" tabindex="-1">Working with Data</a>.</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output icon-scrolling" id="cell-C4HZx7Gndbrh" role="region" aria-label="Cell 11: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed at unknown time"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$040125974$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$040125974$-->executed at unknown time</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter"></pre><pre class="monaco-colorized colab-dark colab-dark" data-lang="notebook-python"><span><span class="mtk18">import</span><span class="mtk1">&nbsp;numpy&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;np</span></span><br><span><span class="mtk18">import</span><span class="mtk1">&nbsp;IPython.display&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;display</span></span><br><span><span class="mtk18">from</span><span class="mtk1">&nbsp;matplotlib&nbsp;</span><span class="mtk18">import</span><span class="mtk1">&nbsp;pyplot&nbsp;</span><span class="mtk18">as</span><span class="mtk1">&nbsp;plt</span></span><br><span><span class="mtk18">import</span><span class="mtk1">&nbsp;io</span></span><br><span><span class="mtk18">import</span><span class="mtk1">&nbsp;base64</span></span><br><span><span></span></span><br><span><span class="mtk1">ys&nbsp;=&nbsp;</span><span class="mtk6">200</span><span class="mtk1">&nbsp;+&nbsp;np.random.randn</span><span class="mtk12">(</span><span class="mtk6">100</span><span class="mtk12">)</span></span><br><span><span class="mtk1">x&nbsp;=&nbsp;</span><span class="mtk12">[</span><span class="mtk1">x&nbsp;</span><span class="mtk18">for</span><span class="mtk1">&nbsp;x&nbsp;</span><span class="mtk17">in</span><span class="mtk1">&nbsp;</span><span class="mtk15">range</span><span class="mtk12">(</span><span class="mtk15">len</span><span class="mtk12">(</span><span class="mtk1">ys</span><span class="mtk12">))]</span></span><br><span><span></span></span><br><span><span class="mtk1">fig&nbsp;=&nbsp;plt.figure</span><span class="mtk12">(</span><span class="mtk1">figsize=</span><span class="mtk12">(</span><span class="mtk6">4</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk6">3</span><span class="mtk12">),</span><span class="mtk1">&nbsp;facecolor=</span><span class="mtk5">'w'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.plot</span><span class="mtk12">(</span><span class="mtk1">x</span><span class="mtk12">,</span><span class="mtk1">&nbsp;ys</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'-'</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.fill_between</span><span class="mtk12">(</span><span class="mtk1">x</span><span class="mtk12">,</span><span class="mtk1">&nbsp;ys</span><span class="mtk12">,</span><span class="mtk1">&nbsp;</span><span class="mtk6">195</span><span class="mtk12">,</span><span class="mtk1">&nbsp;where=</span><span class="mtk12">(</span><span class="mtk1">ys&nbsp;&gt;&nbsp;</span><span class="mtk6">195</span><span class="mtk12">),</span><span class="mtk1">&nbsp;facecolor=</span><span class="mtk5">'g'</span><span class="mtk12">,</span><span class="mtk1">&nbsp;alpha=</span><span class="mtk6">0.6</span><span class="mtk12">)</span></span><br><span><span class="mtk1">plt.title</span><span class="mtk12">(</span><span class="mtk5">"Sample&nbsp;Visualization"</span><span class="mtk12">,</span><span class="mtk1">&nbsp;fontsize=</span><span class="mtk6">10</span><span class="mtk12">)</span></span><br><span><span></span></span><br><span><span class="mtk1">data&nbsp;=&nbsp;io.BytesIO</span><span class="mtk12">()</span></span><br><span><span class="mtk1">plt.savefig</span><span class="mtk12">(</span><span class="mtk1">data</span><span class="mtk12">)</span></span><br><span><span class="mtk1">image&nbsp;=&nbsp;F</span><span class="mtk5">"data:image/png;base64,{base64.b64encode(data.getv</span><span class="mtk5">alue()).decode()}"</span></span><br><span><span class="mtk1">alt&nbsp;=&nbsp;</span><span class="mtk5">"Sample&nbsp;Visualization"</span></span><br><span><span class="mtk1">display.display</span><span class="mtk12">(</span><span class="mtk1">display.Markdown</span><span class="mtk12">(</span><span class="mtk1">F</span><span class="mtk5">"""</span><span class="mtk1">![{alt}]({image})</span><span class="mtk5">"""</span><span class="mtk12">))</span></span><br><span><span class="mtk1">plt.close</span><span class="mtk12">(</span><span class="mtk1">fig</span><span class="mtk12">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$040125974$-->Start coding or <span role="button" class="link">generate</span> with AI.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 11 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$--><svg viewBox="0 0 24 24"><!--?lit$040125974$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$040125974$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$040125974$--><!----><div><!--?lit$040125974$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style="height: 249px;"><div class="outputview" style="height: 249px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./python_files/outputframe.html" class="" tabindex="-1" style="height: 249px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-VYV91hbKwP2J" role="region" aria-label="Cell 12: Text cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p>Colab notebooks execute code on Google's cloud servers, meaning you can leverage the power of Google hardware, including <a href="https://colab.research.google.com/#using-accelerated-hardware" tabindex="-1">GPUs and TPUs</a>, regardless of the power of your machine. All you need is a browser.</p>
<p>For example, if you find yourself waiting for <strong>pandas</strong> code to finish running and want to go faster, you can switch to a GPU Runtime and use libraries like <a href="https://www.google.com/url?q=https%3A%2F%2Frapids.ai%2Fcudf-pandas" target="_blank" rel="nofollow" aria-label="RAPIDS cuDF Link will open in a new tab" tabindex="-1">RAPIDS cuDF</a> that provide zero-code-change acceleration.</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-vwnNlNIEwoZ8" role="region" aria-label="Cell 13: Text cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p>To learn more about accelerating pandas on Colab, see the <a href="https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cudf_pandas_colab_demo.ipynb" target="_blank" rel="nofollow" aria-label="10 minute guide Link will open in a new tab" tabindex="-1">10 minute guide</a> or
 <a href="https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cudf_pandas_stocks_demo.ipynb" target="_blank" rel="nofollow" aria-label="US stock market data analysis demo Link will open in a new tab" tabindex="-1">US stock market data analysis demo</a>.</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-OwuxHmxllTwN" role="region" aria-label="Cell 14: Text cell: Machine learning" style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="markdown-google-sans">

<div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 1 child cell under Machine learning (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 1 child cell under Machine learning (Press &lt;Shift&gt; to also collapse sibling sections)" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 1 child cell under Machine learning (Press &lt;Shift&gt; to also collapse sibling sections)" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h2>Machine learning</h2></div>
</div>

<p>With Colab you can import an image dataset, train an image classifier on it, and evaluate the model, all in just <a href="https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb" target="_blank" rel="nofollow" aria-label="a few lines of code Link will open in a new tab" tabindex="-1">a few lines of code</a>.</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 1 cell hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-ufxBm1yRnruN" role="region" aria-label="Cell 15: Text cell: " style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p>Colab is used extensively in the machine learning community with applications including:</p>
<ul>
<li>Getting started with TensorFlow</li>
<li>Developing and training neural networks</li>
<li>Experimenting with TPUs</li>
<li>Disseminating AI research</li>
<li>Creating tutorials</li>
</ul>
<p>To see sample Colab notebooks that demonstrate machine learning applications, see the <a href="https://colab.research.google.com/#machine-learning-examples" tabindex="-1">machine learning examples</a> below.</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell--Rh3-Vt9Nev9" role="region" aria-label="Cell 16: Text cell: More Resources" style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="markdown-google-sans">

<div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 1 child cell under More Resources (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 1 child cell under More Resources (Press &lt;Shift&gt; to also collapse sibling sections)" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 1 child cell under More Resources (Press &lt;Shift&gt; to also collapse sibling sections)" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h2>More Resources</h2></div>
<h3>Working with Notebooks in Colab</h3>
</div>

<ul>
<li><a href="https://colab.research.google.com/notebooks/basic_features_overview.ipynb" target="_blank" rel="nofollow" aria-label="Overview of Colab Link will open in a new tab" tabindex="-1">Overview of Colab</a></li>
<li><a href="https://colab.research.google.com/notebooks/markdown_guide.ipynb" target="_blank" rel="nofollow" aria-label="Guide to Markdown Link will open in a new tab" tabindex="-1">Guide to Markdown</a></li>
<li><a href="https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb" target="_blank" rel="nofollow" aria-label="Importing libraries and installing dependencies Link will open in a new tab" tabindex="-1">Importing libraries and installing dependencies</a></li>
<li><a href="https://colab.research.google.com/github/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb" target="_blank" rel="nofollow" aria-label="Saving and loading notebooks in GitHub Link will open in a new tab" tabindex="-1">Saving and loading notebooks in GitHub</a></li>
<li><a href="https://colab.research.google.com/notebooks/forms.ipynb" target="_blank" rel="nofollow" aria-label="Interactive forms Link will open in a new tab" tabindex="-1">Interactive forms</a></li>
<li><a href="https://colab.research.google.com/notebooks/widgets.ipynb" target="_blank" rel="nofollow" aria-label="Interactive widgets Link will open in a new tab" tabindex="-1">Interactive widgets</a></li>
</ul>
<div class="markdown-google-sans">

<p><a name="working-with-data"></a></p>
<h3>Working with Data</h3>
</div>

<ul>
<li><a href="https://colab.research.google.com/notebooks/io.ipynb" target="_blank" rel="nofollow" aria-label="Loading data: Drive, Sheets, and Google Cloud Storage Link will open in a new tab" tabindex="-1">Loading data: Drive, Sheets, and Google Cloud Storage</a></li>
<li><a href="https://colab.research.google.com/notebooks/charts.ipynb" target="_blank" rel="nofollow" aria-label="Charts: visualizing data Link will open in a new tab" tabindex="-1">Charts: visualizing data</a></li>
<li><a href="https://colab.research.google.com/notebooks/bigquery.ipynb" target="_blank" rel="nofollow" aria-label="Getting started with BigQuery Link will open in a new tab" tabindex="-1">Getting started with BigQuery</a></li>
</ul>
<div class="markdown-google-sans">

<h3>Machine Learning Crash Course</h3>
<div>

<p>These are a few of the notebooks from Google's online Machine Learning course. See the <a href="https://developers.google.com/machine-learning/crash-course/" target="_blank" rel="nofollow" aria-label="full course website Link will open in a new tab" tabindex="-1">full course website</a> for more.</p>
<ul>
<li><a href="https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/pandas_dataframe_ultraquick_tutorial.ipynb" target="_blank" rel="nofollow" aria-label="Intro to Pandas DataFrame Link will open in a new tab" tabindex="-1">Intro to Pandas DataFrame</a></li>
<li><a href="https://www.google.com/url?q=https%3A%2F%2Fnvda.ws%2Frapids-cudf" target="_blank" rel="nofollow" aria-label="Intro to RAPIDS cuDF to accelerate pandas Link will open in a new tab" tabindex="-1">Intro to RAPIDS cuDF to accelerate pandas</a></li>
<li><a href="https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/linear_regression_with_synthetic_data.ipynb" target="_blank" rel="nofollow" aria-label="Linear regression with tf.keras using synthetic data Link will open in a new tab" tabindex="-1">Linear regression with tf.keras using synthetic data</a></li>
</ul>
<div class="markdown-google-sans">

<p><a name="using-accelerated-hardware"></a></p>
<h3>Using Accelerated Hardware</h3>
</div>

<ul>
<li><a href="https://colab.research.google.com/notebooks/gpu.ipynb" target="_blank" rel="nofollow" aria-label="TensorFlow with GPUs Link will open in a new tab" tabindex="-1">TensorFlow with GPUs</a></li>
<li><a href="https://colab.research.google.com/notebooks/tpu.ipynb" target="_blank" rel="nofollow" aria-label="TensorFlow with TPUs Link will open in a new tab" tabindex="-1">TensorFlow with TPUs</a></li>
</ul>
</div></div></span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 1 cell hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-P-H6Lw1vyNNd" role="region" aria-label="Cell 17: Text cell: Featured examples" style=""><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="markdown-google-sans">

<p><a name="machine-learning-examples"></a></p>
<div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Collapse 0 child cells under Featured examples (Press &lt;Shift&gt; to also collapse sibling sections)" data-aria-label="Collapse 0 child cells under Featured examples (Press &lt;Shift&gt; to also collapse sibling sections)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Collapse 0 child cells under Featured examples (Press &lt;Shift&gt; to also collapse sibling sections)" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h3>Featured examples</h3></div>
</div>

<ul>
<li><a href="https://tensorflow.org/hub/tutorials/tf2_image_retraining" target="_blank" rel="nofollow" aria-label="Retraining an Image Classifier Link will open in a new tab" tabindex="-1">Retraining an Image Classifier</a>: Build a Keras model on top of a pre-trained image classifier to distinguish flowers.</li>
<li><a href="https://tensorflow.org/hub/tutorials/tf2_text_classification" target="_blank" rel="nofollow" aria-label="Text Classification Link will open in a new tab" tabindex="-1">Text Classification</a>: Classify IMDB movie reviews as either <em>positive</em> or <em>negative</em>.</li>
<li><a href="https://tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization" target="_blank" rel="nofollow" aria-label="Style Transfer Link will open in a new tab" tabindex="-1">Style Transfer</a>: Use deep learning to transfer style between images.</li>
<li><a href="https://tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa" target="_blank" rel="nofollow" aria-label="Multilingual Universal Sentence Encoder Q&amp;A Link will open in a new tab" tabindex="-1">Multilingual Universal Sentence Encoder Q&amp;A</a>: Use a machine learning model to answer questions from the SQuAD dataset.</li>
<li><a href="https://tensorflow.org/hub/tutorials/tweening_conv3d" target="_blank" rel="nofollow" aria-label="Video Interpolation Link will open in a new tab" tabindex="-1">Video Interpolation</a>: Predict what happened in a video between the first and the last frame.</li>
</ul>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Run cell" tabindex="-1">
        <span class="execution-count"><!--?lit$040125974$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$040125974$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$040125974$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$040125974$--> <!--?lit$040125974$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="click to expand">↳ 0 cells hidden</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          </div>
          <!--?lit$040125974$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links" tabindex="-1">
        <!--?lit$040125974$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank" tabindex="-1">
        <!--?lit$040125974$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow"></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$040125974$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$040125974$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$040125974$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$040125974$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$040125974$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$040125974$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$040125974$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./python_files/outputframe(1).html" tabindex="-1" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals allow-popups-to-escape-sandbox" src="./python_files/outputframe(2).html" tabindex="-1" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Runtime status bar" style="min-height: inherit;"><template shadowrootmode="open"><!----> <!--?lit$040125974$--><div class="frames"></div>
      <md-icon-button class="visible-on-closed" title="Runtime disconnected" data-aria-label="Runtime disconnected" disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Runtime disconnected" disabled="">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" class="visible-on-closed" status="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$040125974$-->fiber_manual_record</md-icon>
      </md-icon-button>
      <!--?lit$040125974$-->
      <md-icon-button title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close" tabindex="-1">
        <!--?lit$040125974$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$040125974$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$040125974$--><span class="icon"><slot></slot></span>
        <!--?lit$040125974$-->
        <!--?lit$040125974$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button></template></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" inert="" aria-hidden="true" style="display: none; user-select: none;"><!--?lit$040125974$--><div command="new" class=" goog-menuitem " role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->New notebook in Drive<!--?lit$040125974$--></div></div><div command="open" class=" goog-menuitem " role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Open notebook<!--?lit$040125974$--></div></div><div command="import-notebook" class=" goog-menuitem " role="menuitem" id=":4" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Upload notebook<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":5" style="user-select: none;"></div><div command="rename" class=" goog-menuitem " role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Rename<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":7" style="user-select: none;"></div><div command="clone" class=" goog-menuitem " role="menuitem" id=":8" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Save a copy in Drive<!--?lit$040125974$--></div></div><div command="copy-to-gist" class=" goog-menuitem " role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Save a copy as a GitHub Gist<!--?lit$040125974$--></div></div><div command="copy-to-github" class=" goog-menuitem " role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Save a copy in GitHub<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":b" style="user-select: none;"></div><div command="save" class=" goog-menuitem " role="menuitem" id=":c" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Save<!--?lit$040125974$--></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Revision history<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":e" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$040125974$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Print<!--?lit$040125974$--></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" inert="" aria-hidden="true" style="display: none; user-select: none;"><!--?lit$040125974$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Download .ipynb<!--?lit$040125974$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Download .py<!--?lit$040125974$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" inert="" aria-hidden="true" style="display: none; user-select: none;"><!--?lit$040125974$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Undo<!--?lit$040125974$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Redo<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":m" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Select all cells<!--?lit$040125974$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Cut cell or selection<!--?lit$040125974$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Copy cell or selection<!--?lit$040125974$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Paste<!--?lit$040125974$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Delete selected cells<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Find and replace<!--?lit$040125974$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Find next<!--?lit$040125974$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Find previous<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":w" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Notebook settings<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Clear all outputs<!--?lit$040125974$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" inert="" aria-hidden="true" style="display: none; user-select: none;"><!--?lit$040125974$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$040125974$-->Table of contents<!--?lit$040125974$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":12" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Notebook info<!--?lit$040125974$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Executed code history<!--?lit$040125974$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$040125974$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":18" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Collapse sections<!--?lit$040125974$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Expand sections<!--?lit$040125974$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Save collapsed section layout<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1c" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Show/hide code<!--?lit$040125974$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Show/hide output<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1f" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Focus next tab<!--?lit$040125974$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Focus previous tab<!--?lit$040125974$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Move tab to next pane<!--?lit$040125974$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Move tab to previous pane<!--?lit$040125974$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" inert="" aria-hidden="true" style="display: none; user-select: none;"><!--?lit$040125974$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Hide comments<!--?lit$040125974$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":16" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Minimize comments<!--?lit$040125974$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Expand comments<!--?lit$040125974$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" inert="" aria-hidden="true" style="display: none; user-select: none;"><!--?lit$040125974$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Code cell<!--?lit$040125974$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Text cell<!--?lit$040125974$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Section header cell<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1o" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Scratch code cell<!--?lit$040125974$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Code snippets<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1r" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":1s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Add a form field<!--?lit$040125974$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" inert="" aria-hidden="true" style="display: none; user-select: none;"><!--?lit$040125974$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":1u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Run all<!--?lit$040125974$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Run before<!--?lit$040125974$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":1w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Run the focused cell<!--?lit$040125974$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":1x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Run selection<!--?lit$040125974$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Run cell and below<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1z" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Interrupt execution<!--?lit$040125974$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":21" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Restart session<!--?lit$040125974$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Restart session and run all<!--?lit$040125974$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Disconnect and delete runtime<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":24" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":25" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Change runtime type<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":26" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":27" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Manage sessions<!--?lit$040125974$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->View resources<!--?lit$040125974$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->View runtime logs<!--?lit$040125974$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" inert="" aria-hidden="true" style="display: none; user-select: none;"><!--?lit$040125974$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Command palette<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Settings<!--?lit$040125974$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Keyboard shortcuts<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2f" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Diff notebooks<!--?lit$040125974$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$040125974$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" inert="" aria-hidden="true" style="display: none; user-select: none;"><!--?lit$040125974$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Frequently asked questions<!--?lit$040125974$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->View release notes<!--?lit$040125974$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2k" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Search code snippets<!--?lit$040125974$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2l" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Report a bug<!--?lit$040125974$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->Send feedback<!--?lit$040125974$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$040125974$-->View terms of service<!--?lit$040125974$--></div></div></div><div class="thumbnail" inert="" aria-hidden="true"></div><iframe id="apiproxy21b0ae53f9be04f3c9c656297abd40a54eaf02700.13336168" name="apiproxy21b0ae53f9be04f3c9c656297abd40a54eaf02700.13336168" src="./python_files/proxy.html" tabindex="-1" aria-hidden="true" inert="" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><span id="PING_IFRAME_FORM_DETECTION" inert="" aria-hidden="true" style="display: none;"></span><div inert="" aria-hidden="true"><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-moefpklpvnoq" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./python_files/anchor.html" tabindex="-1"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" tabindex="-1" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe tabindex="-1" style="display: none;" src="./python_files/saved_resource.html"></iframe></div><div inert="" aria-hidden="true" style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe src="./python_files/bscframe.html" inert="" aria-hidden="true" tabindex="-1" style="display: none;"></iframe><script src="./python_files/survey_binary__en.js.download" nonce="" type="text/javascript" data-survey-binary="" gapi_processed="true"></script><iframe src="./python_files/saved_resource(1).html" id="google-hats-survey" name="google-hats-survey" title="Google Survey" aria-live="polite" style="color-scheme: normal; height: 422.667px; max-height: 100%; transition: 0.25s; bottom: 8px; right: 24px; width: 363px; background: rgb(48, 49, 53); outline: transparent solid 3px; box-shadow: rgba(0, 0, 0, 0.14) 0px 16px 24px 2px, rgba(0, 0, 0, 0.12) 0px 6px 30px 5px, rgba(0, 0, 0, 0.2) 0px 8px 10px -5px; position: fixed; border: none; border-radius: 8px;" aria-label="User Survey Dialog, Overall, how satisfied are you with Colaboratory?" inert="" aria-hidden="true" tabindex="-1"></iframe><iframe id="hfcr" src="./python_files/RotateCookiesPage.html" inert="" aria-hidden="true" tabindex="-1" style="display: none;"></iframe></body></html>