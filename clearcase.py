import os
import sublime
import sublime_plugin

class ClearcaseCommand(sublime_plugin.WindowCommand):
    def run(self, cmd):
        if len(self.window.active_view().file_name()) > 0:
            self.window.run_command('exec', {'cmd': cmd})

    def is_enabled(self):
        return self.window.active_view().file_name() and len(self.window.active_view().file_name()) > 0

class ClearcaseExplorerCommand(ClearcaseCommand):
    def run(self):
        cmd = ['clearexplorer', os.path.dirname(self.window.active_view().file_name())]
        super(ClearcaseExplorerCommand, self).run(cmd)

class ClearcaseCheckoutCommand(ClearcaseCommand):
    def run(self):
        cmd = ['cleardlg', '/checkout', self.window.active_view().file_name()]
        super(ClearcaseCheckoutCommand, self).run(cmd)

class ClearcaseCheckinCommand(ClearcaseCommand):
    def run(self):
        cmd = ['cleardlg', '/checkin', self.window.active_view().file_name()]
        super(ClearcaseCheckinCommand, self).run(cmd)

class ClearcaseVtreeCommand(ClearcaseCommand):
    def run(self):
        cmd = ['cleartool', 'lsvtree', '-graphical', self.window.active_view().file_name()]
        super(ClearcaseVtreeCommand, self).run(cmd)

class ClearcasePrevCommand(ClearcaseCommand):
    def run(self):
        cmd = ['cleartool', 'diff', '-graph', '-pred', self.window.active_view().file_name()]
        super(ClearcasePrevCommand, self).run(cmd)

class ClearcaseUncoCommand(ClearcaseCommand):
    def run(self):
        cmd = ['cleartool', 'unco', self.window.active_view().file_name()]
        super(ClearcaseUncoCommand, self).run(cmd)

class ClearcaseAnnotateCommand(ClearcaseCommand):
    def run(self):
        out = '%s.ann' % self.window.active_view().file_name()
        cmd = ['cleartool', 'annotate', '-short', '-out', out, self.window.active_view().file_name()]
        super(ClearcaseAnnotateCommand, self).run(cmd)
        self.window.open_file(out)
