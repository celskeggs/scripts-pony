<%inherit file="scriptspony.templates.master"/>

%if hosts is not None:
  <h3>Hostnames for the ${locker} locker</h3>

  <p>
    <table border="1">
      <tr><th>Hostname</th><th>Path</th></tr>
      %for host,path in hosts:
        <form method="post">
          <tr>
            <td>${host}</td><td>${path}</td>
            %if host not in (locker+'.scripts.mit.edu',):
              <td><a href="${tg.url('/edit/'+locker+'/'+host)}">edit</a></td>
            %endif
          </tr>
        </form>
      %endfor
    </table>
    
    Paths are relative to the top directory for the 
    appropriate service; for example, 
    <tt>/mit/${locker}/web_scripts/</tt> for web scripts or 
    <tt>/mit/${locker}/Scripts/svn/</tt> for Subversion.
  </p>
  <p>
    <a href="${tg.url('/new/'+locker)}">Request a new hostname</a> for the ${locker} locker

<hr />
  <p> You can choose a different locker that you've already managed: </p>
  <ul>
  %for l in user_info.lockers:
  <li>
  %if l == locker:
  <b>${l}</b>
  %else:
  <a href="${tg.url('/index', locker=l)}">${l | h}</a>
  %endif
  </li>
  %endfor
  </ul>

  </p>
  <form action="${tg.url('/index')}">
   Or switch to managing the <input type="text" name="locker" value="${locker}" /> locker
    <input type="submit" value="Switch" />
  </form>
%else:
  <p>Scripts Pony!  This useful tool lets you configure all the
  hostnames you use for scripts.mit.edu websites.  Log in with your MIT
  certificates above.</p>
%endif
