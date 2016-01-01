docker-dev-env
==============

A development environment based on docker

Containerized Developement Environment (CDE)

mostly junk at this point

## Architecture
As a basic tenet, a developer/user may have more than one host machine involved in their development experience. For example, a laptop, a work desktop, and home desktop. All the projects that a user manages should be available to all the hosts in the CDE. However, a user should be able to select which projects appear where. Two examples, only work projects may be available on the work computer; only active projects are available on the laptop. 

### Storage
A storage container should be provided that handles the storage needs of any of the applications used in the CDE. The storage should be offered as docker mountable volumes. The storage should manage regular backups, per mount (e.g. a git repo may have different backup rules than browser history). The storage should also manage the replication of the available projects to each host participating in the CDE. All of these functions should be provided as a container which may or may not be the same container as the storage itself. 

### Project Context
Every proejct should be able to store and recreate the context in which it was last worked. For example, the open browser tabs, editors, terminals, etc should be both saved on project close and opened when a project is opened.

### Task Context 
Each project may have one or more tasks associated with the project. The tasks should be able to store the context in which they were last operated on and open that context when launched. Similar to the [Project Context]() referenced elsewhere. Also similar to the [Mylyn](http://www.eclipse.org/mylyn/) functionality in Eclipse. 