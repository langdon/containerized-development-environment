#! /usr/bin/env python
from subprocess import check_output, Popen, CalledProcessError, STDOUT
import time
import argparse
from gi.repository import Notify

parser = argparse.ArgumentParser(description='A script for putting VMs to sleep when you sleep your machine.',
    epilog="""You can create a link to this script in /usr/lib/systemd/system-sleep/ (assuming a distro layout 
    like Fedora and systemd). If you do, the script will attempt to "save" all your running VMs when you 
    put your machine to sleep. I do this (even though virsh/libvirt will actually sleep them and wake them up
    again on its own because when I come back up, I often am doing something else or on battery and forget I 
    have a whole mess of VMs running. Technically, this script has arguments, but they are really just to 
    support the params systemd passes.""")

with open('/var/log/vm-suspend.log', 'a+') as log:
    log.write("Starting work %s\n" % time.strftime("%H:%M:%S"))

    parser.add_argument('when',  nargs='?', default="", help='pre or post')
    parser.add_argument('type',  nargs='?', default="", help='suspend or hibernate')
    
    args = parser.parse_args()
    log.write("Received %s and %s as args\n" % (args.when, args.type))

    Notify.init ("vm suspend")
  
    if args.when == "pre":
        vms = check_output("virsh list --name", shell=True)
        vms = vms.split('\n')
        log.write("Found these vms: %s \n" % vms)
        for vm in vms:
            if (vm != ""):
		try:
			cmd_to_run = "virsh managedsave %s --running"
			#cmd_to_run = "virsh shutdown %s 2>&1"
                	msgs = check_output(cmd_to_run % vm, stderr=STDOUT, shell=True)
                	log.write("Ran: %s ; Stopped %s: {output: \"%s\"} \n" % (cmd_to_run, vms, msgs))
                        vm_suspend=Notify.Notification.new ("VM Suspend Job", "%s VMs have been suspended" % len(vms), "dialog-alert")
		except CalledProcessError as e:
	                log.write("Ran %s on %s: Failed output: %s \n" % (cmd_to_run, vm, e.output))
                        vm_suspend=Notify.Notification.new ("VM Suspend Job", "Job failed, check \"tail /var/log/vm-suspend.log\" for details", "dialog-error")

                vm_suspend.show()

    log.write("Completed work %s\n" % time.strftime("%H:%M:%S"))
