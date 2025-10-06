from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Video
from .forms import VideoForm

def video_list(request):
    """Display all videos"""
    videos = Video.objects.all()
    return render(request, 'assignment2_app/video_list.html', {'videos': videos})

def video_detail(request, pk):
    """Display details of a specific video"""
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'assignment2_app/video_detail.html', {'video': video})

def video_create(request):
    """Create a new video"""
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video created successfully!')
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'assignment2_app/video_form.html', {'form': form, 'title': 'Add New Video'})

def video_update(request, pk):
    """Update an existing video"""
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video updated successfully!')
            return redirect('video_list')
    else:
        form = VideoForm(instance=video)
    return render(request, 'assignment2_app/video_form.html', {'form': form, 'title': 'Update Video'})

def video_delete(request, pk):
    """Delete a video"""
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        messages.success(request, 'Video deleted successfully!')
        return redirect('video_list')
    return render(request, 'assignment2_app/video_confirm_delete.html', {'video': video})
